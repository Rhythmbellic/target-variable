#importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#here or target variable is sale price so we will perform our functions on it
data=pd.read_csv('1. Regression - Module - (Housing Prices).csv')
#overview of target variable
data['Sale Price'].head(10)
data['Sale Price'].tail(10)
data['Sale Price']
data['Sale Price'].describe()
#we come to know there are 4 missing values and data is not equally distributed
# to make data equally distributed we will deal with outliers first
#let see outlier by ploting first
plt.scatter(x=data['ID'],y=data['Sale Price'])
#lets remove outliers by putting limits
Q3=645000
Q1=321950
IQR=Q3-Q1
lower_limit=Q1-1.5*IQR
upper_limit=Q3+1.5*IQR
a=data['Sale Price'].min()
b=data['Sale Price'].max()
if(lower_limit<a):
    lower_limit=data['Sale Price'].min()
if(upper_limit>b):
    upper_limit=data['Sale Price'].max()
#now to see visually we will use seaburn lib for boxplot as matplotlib can't ignore missing values
sns.boxplot(x=data['Sale Price'])
#we don"t use deleting method for target variable for outlier and use imputing
def limit_imputer(value):
    if value>upper_limit:
        return upper_limit
    if value<lower_limit:
        return lower_limit
    else:
        return value
data['Sale Price']=data['Sale Price'].apply(limit_imputer)
data['Sale Price'].describe()  #we can see we have treated outliers
#now we will deal with missing values we can do it by to method
#1.by deleting whole row
#2.by imputing values
#we will not impute values as it will make our stats more with rong values so we will delete it
data.dropna(inplace=True,axis=0,subset=['Sale Price'])
data.info()#we can see missing values row has been dropped
plt.hist(data['Sale Price'],bins=10,color='green')
