# Machine Learning Case Study,EDA and Model Building

# Bank Marketing Prediction

## **Introduction**

The aim of this project is to analyzed data from the BankMarketing Data Set.  This data set is related to direct marketing campaigns of a Portuguese banking institution, conducted via phone calls. The first part of our project involved describing and visualizing the data, while the second part focused on using data classification models.


(https://archive.ics.uci.edu/ml/datasets/bank+marketing#)


## **Goal**  

The classification goal is to analysis the bank dataset to optimize its operations and strategies to attract more customers to subscribe to term deposits.
We have a classification problem and target is a binary variable (yes/no) 


 ## **File Description**
 
**Bank1**: Understanding the Dataset

**Bank2**: Bank_EDA Insights on Exploratory Data Analysis.

**Bank3**: Preprocessing & Modeling: Building theree models and it's evaluation part.

**Bank4** : Preprocessing & Modeling_Over&UnderSampled: Applying oversampling techniques like SMOTE, SVMSMOTE & undersampling to assess whether they can improve the misclassification issue in this imbalanced data set.

**Bank5**: Modeling on Socio-Economic Attributes: (additional bank dataset) to check if they can affect misclassification and decrease false negatives.

## **Performance Metric Used**

We focused on **AUC** over accuracy because the dataset is imbalanced with the majority class being "no". Using accuracy as a metric can result in a high accuracy score even for a random model. However, AUC considers both **true positive rate** and **false positive rate**, and only a model with TPR and FPR well above the random line in the ROC curve will have a good AUC. Accuracy cannot guarantee this.
