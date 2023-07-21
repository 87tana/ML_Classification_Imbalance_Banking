
### import required library
import os
import argparse
import pandas as pd
import numpy as np
import pickle


from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GridSearchCV

from sklearn.utils.class_weight import compute_class_weight
from sklearn.preprocessing import RobustScaler

import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', None)



RANDOM_STATE =42



def preprocess(df):
    """
    Pre-Processing
    """

    # According to EDA, some features like day,month have no affect on subscribition
    df.drop(['day', 'month'], axis=1, inplace=True)

    # Impute the "unknown" values
    columns_to_impute = ['job', 'education']

    # Loop over each column and impute unknown value
    for i in columns_to_impute:
        # Compute the normalized value counts for non-unknown values
        value_counts = df.loc[df[i] != 'unknown', i].value_counts(normalize=True)
        df.loc[df[i] == 'unknown', i] = np.random.choice(value_counts.index, 
                                                        p = value_counts.values, size = df.loc[df[i]  == 'unknown'].shape[0] )
    # 'unknown', 'failure', and 'other' indicate a lack of success in the previous marketing campaign
    # We are replacing these values with 'not success' to simplify the analysis
    # Note that the 'success' values are retained as-is
    df['poutcome'] = df['poutcome'].replace({'unknown':'not success', 'failure':'not success', 'other':'not success'})


    # Transfer some columns

    df = df.rename(columns={'y': 'deposit'}) # Rename the target value
    df['deposit'] = df['deposit'].map({'yes': 1, 'no': 0}) # Define new columns for deposit yes and no

    df['duration'] = df['duration'].apply(lambda n: n / 60).round(2) #Change the unit of 'duration' from sec to min


    # Dummy Encoding

    #Convert categorical variables to dummy variables
    df_dummy = pd.get_dummies(df[['job', 'marital', 'education', 'poutcome', 'contact']])

    # Drop original categorical columns
    df = df.drop(['job', 'marital', 'education', 'poutcome', 'contact'], axis=1)

    #First Convert the object to Boolean
    df['housing'] = df['housing'].astype(bool)
    df['loan'] = df['loan'].astype(bool)
    df['default'] = df['default'].astype(bool)

    #Convert Boolean variables to integers
    df['housing'] = df['housing'].astype('int')
    df['loan'] = df['loan'].astype('int')
    df['default'] = df['default'].astype('int')

    # Concatenate encoded categorical variables with numerical variables
    df = pd.concat([df_dummy, df], axis=1)

    return df



def feature_scaling(X):
    """
    Feature Scaling
    """
    scaler = RobustScaler()
    x_scaled = scaler.fit_transform(X)
    columns = X.columns
    X = pd.DataFrame(x_scaled, columns=columns)

    return X



def randomforest_train(X, y):

    print('Train RandomForest ...')
    # Define the random forest classifier 
    rf_1 = RandomForestClassifier(random_state=RANDOM_STATE)



    # Define the class_weight (gives equall importance to the classes)
    class_weights = compute_class_weight(class_weight='balanced', classes=np.unique(y), y=y)
    class_weights_rf = [{0:class_weights[0],1:class_weights[1]}]
    n_estimators = [10, 30, 50, 70, 90] # Number of trees in random forest
    max_features = ['log2', 'sqrt'] # Number of features to consider at every split
    max_depth = [3, 5, 7, 9] # Maximum number of levels in tree
    # Minimum number of samples required to split a node
    #min_samples_split = [2, 5, 10]
    # Minimum number of samples required at each leaf node
    #min_samples_leaf = [1, 2, 4]


    """
    Grid Search
    """
    print('Define and fit grid search to the training data ...')

    parameters = {'n_estimators': n_estimators, 
                'criterion' : [ 'entropy'], 
                'max_depth': max_depth, 
                'max_features': max_features,
                'class_weight':class_weights_rf}


    # Create a splitter object
    stratified = StratifiedShuffleSplit(n_splits=5,test_size=0.2, random_state=RANDOM_STATE)

    # Define the GridSearch Object
    grid_search = GridSearchCV(rf_1,parameters, cv=stratified, scoring='f1_macro', n_jobs=-1)

    # Fit grid search to training data
    grid_search.fit(X, y)

    # Get the best estimator and score
    best_rf = grid_search.best_estimator_  #obtain the best estimator from the grid search 
    best_score = grid_search.best_score_


    print("Best F1 score: {:.2f}%".format(best_score*100))

    best_params = grid_search.best_params_
    rf = RandomForestClassifier(random_state=RANDOM_STATE, n_estimators=best_params['n_estimators'], criterion=best_params['criterion'],
                                max_depth=best_params['max_depth'], max_features=best_params['max_features'], class_weight=best_params['class_weight'])
    
    rf.fit(X, y)

    # Evaluate the performance on the training data
    train_accuracy = rf.score(X, y)
    print("Training accuracy: {:.2f}%".format(train_accuracy*100))
    



    return rf


### Path to the input data and the output model
#data_path = '../bank-full.csv'
#output_path = './'


parser = argparse.ArgumentParser(description='Train a model.')
parser.add_argument('--data', type = str, required=True, help='Input csv data file.')
parser.add_argument('--outdir', type = str, required=True, help='Output directory path.')
args = parser.parse_args()


### Read the data
df = pd.read_csv(args.data, sep = ';')

### Preprocess data
df = preprocess(df)

### Define observation and target values
X = df.drop('deposit',axis=1)
y = df['deposit']

### Scale features
X = feature_scaling(X)


trained_model = randomforest_train(X, y)


# save randomforest model
with open(os.path.join(args.outdir,'model.pkl'),'wb') as f:
          pickle.dump(trained_model,f)