import pandas as pd
import numpy as np


fireData = pd.read_csv('Fire_Department_Calls_for_Service.csv')
fireData.info()

fireData = fireData.iloc[:1000, :]

len(fireData)
fireData.info()
fireData.describe()

def describe(dataset):
    dataLength = len(dataset)
    print(f"There are {dataLength} number of rows in this dataset")
    dataAverage = dataset["Number of Alarms"].mean()
    print(f"The average for this dataset is {dataAverage}")
    dataShape = dataset.shape
    print(f"This dataset shape is {dataShape}.")
    dataDescribe = dataset.describe()
    print(f"An overview of this datasets basic stastics includes {dataDescribe}.")

describe(fireData)

def filterCallType(dataset):
    callType = dataset["Call Type"].value_counts
    print(f"Counts for each of the call types{callType}.")

filterCallType(fireData)

def filterUnitId(dataset):
    unitId = dataset["Unit ID"].value_counts
    print(unitId)

filterUnitId(fireData)

def distributionInfo(dataset):
    distInfo = dataset["Analysis Neighborhoods"].std()
    print(distInfo)

distributionInfo(fireData)

def nullValue(dataset):
    nullCheck = dataset['Call Number'].isnull()
    print(nullValue)

nullValue(fireData)

