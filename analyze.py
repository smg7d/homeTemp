import os, sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime


dataFiles = ["tempData1.csv", "tempData2.csv", "tempData3.csv", "tempData4.csv", "tempData5.csv"]

fullList = []

for thisfile in dataFiles:
	#read in data frame
	tempDF = pd.read_csv(thisfile, header=None, names=['temp', 'date'])

	#format the date column
	tempDF['date'] = pd.to_datetime(tempDF['date'])

	#set the date as the index
	tempDF = tempDF.set_index('date')

	#append it
	fullList.append(tempDF)

#put all of them together
fullData = pd.concat(fullList)

#create the axis object and format the plot
palette = sns.color_palette("mako_r", 1)
ax = sns.lineplot(data=fullData, palette=palette)
ax.xaxis.set_major_locator(mdates.AutoDateLocator()) #set start of x axis
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d')) #format the x axis labels
ax.set(xlabel='Date', ylabel='Temperature (Fahrenheit)', title='House Temperature Data') #add axis labels
ax.legend_.remove() #take out the legend


plt.savefig('houseTempData')