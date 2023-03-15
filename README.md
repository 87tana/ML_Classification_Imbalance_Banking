# Exploratory Data Analysis and Model Building - Bank Marketing Campaign

## **Data Description**

This dataset(https://archive.ics.uci.edu/ml/datasets/bank+marketing#) gives information about a marketing campaign of a financial institution. 
The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, If the client says yes to opening the term deposit account, the target variable 'y' is marked as 'yes', else 'no'.

The analysis help the bank optimize its operations and strategies to attract more customers to subscribe to term deposits.
We have a classification problem and target is a binary variable (yes/no)

## **Goal**  

Find the best strategies to improve for the next marketing campaign. How can the financial institution have greater effectiveness for future marketing campaigns? In order to answer this, we have to analyze the last marketing campaign the bank performed and identify the patterns that will help us find conclusions in order to develop future strategies


# Understanding the DataSet

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

**Other features**

campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)

pdays: number of days that passed by after the client was last contacted from a previous campaign 

previous: number of contacts performed before this campaign and for this client (numeric)

poutcome: outcome of the previous marketing campaign (categorical)

**Target value**

y (deposit) : Target value

## **Missing Values**

There are several missing values in some categorical attributes, all coded with the "unknown" label. 
These missing values can be treated as a possible class label or remove them by applying imputation techniques.

 There are not that much insights we can gain from the descriptive dataset since most of our descriptive data is located not in the "numeric" columns but in the "categorical columns".
