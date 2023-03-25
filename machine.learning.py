from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np
dataset=pd.read_csv('placement.csv')
print( dataset)
print("------------------------------------------------------------------------------------")

df=dataset.copy()
print(df)
# change any column datatype
dataset["workex"]=(dataset["workex"]=="Yes").astype(int)
print(dataset)
d=dataset.columns
print(d)
print("------------------------------------------------------------------------------------")

d1=dataset.shape
print(d1)
print("-------------------------------------------------------------------------------------")

d2=dataset.dtypes
print(d2)
print("--------------------------------------------------------------------------------------")

d3=dataset.head()
print(d3)
print("--------------------------------------------------------------------------------------")

d4=dataset.tail()
print(d4)
print("--------------------------------------------------------------------------------------")

d5=dataset.describe()
print(d5)
print("---------------------------------------------------------------------------------------")

d6=dataset.isnull()
print(d6)
print("---------------------------------------------------------------------------------------")

d7=dataset.isnull().sum()
print(d7)

for column in dataset.columns:
    if dataset[column].dtype!='object' and dataset[column].isnull().sum():
        mean=dataset[column].mean()
        dataset[column].fillna(mean,inplace=True)

print(dataset)
print(dataset.isnull().sum())

for column in dataset.columns:
    if dataset[column].dtype=='object' and dataset[column].isnull().sum():
        frequent=dataset[column].value_count()
        dataset[column].fillna(frequent.index[0],inplace=True)

print(dataset)
print(dataset.isnull().sum())



# dataset.drop([1],axis=0,inplace=True)
# print(dataset)

# dataset.drop(['salary'],axis=1,inplace=True)
# print(dataset)

