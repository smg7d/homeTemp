import os, sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


dataFiles = ["tempData1.csv", "tempData2.csv", "tempData3.csv", "tempData4.csv", "tempData5.csv"]

fullList = []

for thisfile in dataFiles:
	tempDF = pd.read_csv(thisfile, header=None, names=['temp', 'date'], index_col=1)
	fullList.append(tempDF)

fullData = pd.concat(fullList)

ax = sns.lineplot(data=fullData)
plt.show()