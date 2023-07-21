import pandas as pd
import numpy as np
import pickle
import argparse

from sklearn.metrics import f1_score
from sklearn.preprocessing import RobustScaler




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




parser = argparse.ArgumentParser(description='Test a model.')
parser.add_argument('--data', type = str, required=True, help='Input csv data file.')
parser.add_argument('--model', type = str, required=True, help='Model pkl file.')
parser.add_argument('--outdir', type = str, required=False, help='Output directory path.')
args = parser.parse_args()



### Read the data
df = pd.read_csv(args.data, sep = ';')

### Preprocess data
df = preprocess(df)

model = pickle.load(open(args.model,'rb'))

### Define observation and target values
X = df.drop('deposit',axis=1)
y = df['deposit']

### Scale features
X = feature_scaling(X)

# Evaluate the best estimator on the test data
y_pred = model.predict(X)
test_score = f1_score(y, y_pred)


print("Test F1 score: {:.2f}%".format(test_score*100))
print("Test Acuracy: {:.2f}%".format(model.score(X, y)*100))



"""
## Confusion Matrix
def plot_confusion_matrix(y_val, y_pred, labels=None):

    Plot a confusion matrix for the given true and predicted labels.
    Optionally, provide a list of label names to use for the plot.

    if labels is None:
        labels = np.unique(y_pred)
    cm = confusion_matrix(y_val, y_pred, labels=labels)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='g', cmap='Blues', ax=ax)
    ax.set_xlabel('Predicted Labels')
    ax.set_ylabel('True Labels')
    ax.set_xticklabels(labels)
    ax.set_yticklabels(labels)
    ax.set_title('Confusion Matrix')
    plt.show()

"""