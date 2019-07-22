import os, sys
import pandas as pd

dataFiles = ["tempData2.csv", "tempData3.csv", "tempData4.csv", "tempData5.csv"]

data = pd.read_csv("tempData1.csv") #create the initial dataframe

for file in dataFiles:
	data.append(pd.read_csv(file))

print(data.tail())