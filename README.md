# Machine Learning Case Study,EDA and Model Building - Bank Marketing Prediction

## **Data Description**

This dataset(https://archive.ics.uci.edu/ml/datasets/bank+marketing#) gives information about a marketing campaign of a financial institution. 
The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, If the client says yes to opening the term deposit account, the target variable 'y' is marked as 'yes', else 'no'.

The analysis help the bank optimize its operations and strategies to attract more customers to subscribe to term deposits.
We have a classification problem and target is a binary variable (yes/no)

## **Goal**  

-  The classification goal is to predict if the client will subscribe a term deposit (target variable y). 

## **Type of Machine Learning problem**

This is a **binary classification** problem where the task is to predict whether a customer will subscribe to a term deposit or not. The two classes are "yes" which indiacate that the customer subscribed and "no" which indicate that the customer did not subscribe.

## **Performance Metric Used**

We focused on **AUC** over accuracy because the dataset is imbalanced with the majority class being "no". Using accuracy as a metric can result in a high accuracy score even for a random model. However, AUC considers both **true positive rate** and **false positive rate**, and only a model with TPR and FPR well above the random line in the ROC curve will have a good AUC. Accuracy cannot guarantee this.

## Understanding the DataSet

**Bank client Data**:

Age:(numeric)

Balance : average yearly balance in euros

Job: type of job (categorical)

Marital: marital status (categorical)

Education (categorical)

Default: has credit in default? (categorical: 'no', 'yes', 'unknown')

Housing: has housing loan? (categorical: 'no', 'yes', 'unknown')

Loan: has personal loan? (categorical: 'no', 'yes', 'unknown')

**Related to the last contact of the current campaign**:

Contact: contact communication type (categorical)

Month: last contact month of year (categorical)

Day: last contact day of the week (categorical)

Duration: last contact duration, in seconds (numeric)

**Other Features**

campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)

pdays: number of days that passed by after the client was last contacted from a previous campaign 

previous: number of contacts performed before this campaign and for this client (numeric)

poutcome: outcome of the previous marketing campaign (categorical)

**Social and Economic context attributes**


emp.var.rate: employment variation rate — quarterly indicator (numeric)

cons.price.idx: consumer price index — monthly indicator (numeric)

cons.conf.idx: consumer confidence index — monthly indicator (numeric)

euribor3m: euribor 3 month rate — daily indicator (numeric)

nr.employed: number of employees — quarterly indicator (numeric)

**Target value**

y (deposit) : Target value

## **Missing Values**

The categorical attributes have missing values labeled as **"unknown"**. These values can be treated as a class or imputed.
 
 ## **File Description**

**EDA

**Preprocessing & 
