# Machine Learning Case Study,EDA and Model Building

# Bank Marketing Prediction

## **Introduction**

Old marketing methods didn't help banks increase their enterprise. therefore, European banks tend to offer long-term deposits with good interest rates through direct marketing, but reaching out to many people is time-consuming and has low success rates. 
Banks are now seeking solutions to improve efficiency and increase success rates. 
The Portuguese Banking Institution has provided data on marketing campaigns conducted over the phone.


Multiple contacts with clients were often necessary to determine if they would subscribe(‘yes’ or ‘no’) to the bank's term deposit product.


- Source of Data: [Bank-Marketing](https://archive.ics.uci.edu/ml/datasets/bank+marketing#)


## **Goal**  

The goal is to develop a ML model that can effectively classify whether a client subscribes to longer-term deposits by analyzing input features and identifying unknown patterns.


## **Objectives**

- Which demographics are more likely to open term deposits, and how can the bank leverage this information to increase subscription rates?


- How does marital status affect the likelihood of opening accounts, and how can the bank use this knowledge to improve its marketing strategies?


- What is the success rate of repeat marketing campaigns, and how can the bank improve subscription rates by leveraging this knowledge?


- How many times should the bank contact customers to maximize subscription rates, and how can it optimize its communication channels for maximum effectiveness?


- How can the bank leverage recency to improve customer memory and increase subscription rates, particularly with respect to customers' account balances and ages?


- How can the bank analyze the relationship between the duration of a call and customer age to develop more targeted marketing strategies for different age groups?


 ## **File Description**
 
**Bank1**: Understanding the Dataset

**Bank2**: Bank_EDA Insights on Exploratory Data Analysis.

**Bank3**: Preprocessing & Modeling: Building theree models and it's evaluation part.

**Bank4** : Preprocessing & Modeling_Over&UnderSampled: Applying oversampling techniques like SMOTE, SVMSMOTE & undersampling to assess whether they can improve the misclassification issue in this imbalanced data set.

**Bank5**: Modeling on Socio-Economic Attributes: (additional bank dataset) to check if they can affect misclassification and decrease false negatives.

## **Performance Metric Used**

We focused on **AUC** over accuracy because the dataset is imbalanced with the majority class being "no". Using accuracy as a metric can result in a high accuracy score even for a random model. However, AUC considers both **true positive rate** and **false positive rate**, and only a model with TPR and FPR well above the random line in the ROC curve will have a good AUC. Accuracy cannot guarantee this.



