# Machine Learning Case Study, EDA and Model Building, Imbalance Data

# Bank Marketing Prediction

<p align="center">
    <img width="400" src="Rincian-Biaya-Operasi-Tahi-Lalat-di-Erha-Clinic-300x168.jpg" alt="Material Bread logo">
</p>



## **Introduction**

Old marketing methods didn't help banks increase their enterprise. therefore, European banks tend to offer long-term deposits with good interest rates through direct marketing, but reaching out to many people is time-consuming and has low success rates. 
Banks are now seeking solutions to improve efficiency and increase success rates. 
The Portuguese Banking Institution has provided data on marketing campaigns conducted over the phone.


Multiple contacts with clients were often necessary to determine if they would subscribe(‘yes’ or ‘no’) to the bank's term deposit product.


- Source of Data: [Bank-Marketing](https://archive.ics.uci.edu/ml/datasets/bank+marketing#)


## **Goal**  

The goal is to develop a ML model that can effectively classify whether a client subscribes to longer-term deposits by analyzing input features and identifying unknown patterns.

## **What is a Term Deposit?**

Term deposit is a saving option where you lock away your money for a fixed term and earn a guaranteed interest rate but can't access the money until the term is up.


## **What are the benefits of term deposits for both banks and customers?**

Bank: Stable and Predictable funding source and helps reduce their liquidity risk.


Customer: Secure and low-risk investment option, Guaranteed rate of return


Overall: provide a win-win situation for both banks and customers by offering a reliable source.


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

**Bank3**: Preprocessing and Modeling: Building theree models and it's evaluation part.

**Bank4** : Preprocessing and Modeling_Over&UnderSampled: Applying oversampling techniques like SMOTE, oversampling and undersampling to assess whether they can improve the misclassification issue in this imbalanced data set.

**Bank5**: Modeling on Socio-Economic Attributes: (additional bank dataset) to check if they can affect misclassification and decrease false negatives.

## **Performance Metric Used**


- AUC is a better metric than accuracy for imbalanced datasets, as accuracy can be high even for a random model


- AUC considers both true positive rate and false positive rate, making it a more reliable metric


- The **Random Forest model** demonstrated better **recall and f1-score** for the **minority class**, which is important for predicting subscription to term deposits
It is advisable for the bank to utilize the Random Forest model


- Hyperparameter tuning techniques can be employed to further improve the model's performance



<p align="center">
    <img width="400" src="ROC_on_allfeatures.png" alt="Material Bread logo">  
</p>


