
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **sports or athletics** (see below) for the region of **Ann Arbor, Michigan, United States**, or **United States** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Ann Arbor, Michigan, United States** to Ann Arbor, USA. In that case at least one source file must be about **Ann Arbor, Michigan, United States**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Ann Arbor, Michigan, United States** and **sports or athletics**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **sports or athletics**?  For this category we are interested in sporting events or athletics broadly, please feel free to creatively interpret the category when building your research question!
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[5]:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

###############################################################################
#loading the dataset
df1=pd.read_csv("week2.csv") 
df=df1.copy()

###############################################################################
#changing date column from object format to datetime format
df['Date'] = pd.to_datetime(df['Date'])
print('datatype of Date column is ',df['Date'].dtypes)
#plotting Date vs Close Price of the stock
df.plot(kind='line',x='Date',y='Close Price')
plt.show()

###############################################################################

#plotting a stem plot of change in stock price vs time
plt.stem(df['Date'],df['Day_Perc_Change'])
plt.show()

###############################################################################

#plotting Daily Volume vs Date of the stock
df.plot(kind='line',x='Date',y='Total Traded Quantity')
plt.show()

###############################################################################

#plotting trend values in pie chart
dftrend = df[['Total Traded Quantity','Trend']]
trend=dftrend.groupby(dftrend['Trend']).size()
trend.plot.pie(figsize=(6,6),autopct='%0.2f')
#plotting bar chart of median value
dfmedian=dftrend.groupby(dftrend['Trend']).median()
dfmedian.plot(kind='bar', title ="Median", figsize=(5, 5), legend=True, fontsize=12)
plt.show()
#plotting bar chart of mean values
dftrend=dftrend.groupby(dftrend['Trend']).mean()
dftrend.plot(kind='bar', title ="Mean", figsize=(5,5), legend=True, fontsize=12,color='r')
plt.show()

###############################################################################

#plotting histogram of Day_Perc_Change column
x=df['Day_Perc_Change']
plt.hist(x, bins=30,color='yellow')
plt.show()

###############################################################################

#loading 5 stocks
bajfinance=pd.read_csv("BAJFINANCE.csv") 
infy=pd.read_csv("INFY.csv")
lt=pd.read_csv("LT.csv") 
reliance=pd.read_csv("RELIANCE.csv") 
tcs=pd.read_csv("TCS.csv") 
#creating dataframe with closing price of all stocks
close_price=pd.DataFrame(index=range(len(bajfinance['Close Price'])))
close_price['bajaj_close']=bajfinance[['Close Price']]
close_price['infy_close']=infy[['Close Price']]
close_price['lt_close']=lt[['Close Price']]
close_price['reliance_close']=reliance[['Close Price']]
close_price['tcs_close']=tcs[['Close Price']]
#creating dataframe with percentage change of all stocks
percentage_change=pd.DataFrame(index=range(len(bajfinance['Close Price'])))
percentage_change['bajaj_change']=close_price['bajaj_close'].pct_change()
percentage_change['infy_change']=close_price['infy_close'].pct_change()
percentage_change['lt_change']=close_price['lt_close'].pct_change()
percentage_change['reliance_change']=close_price['reliance_close'].pct_change()
percentage_change['tcs_change']=close_price['tcs_close'].pct_change()
#dropping NAN values
percentage_change=percentage_change.dropna()
#plotting correlogram of percentage_change dataframe
sns.pairplot(percentage_change,height=2)
plt.show()

###############################################################################

roll_avg=pd.DataFrame(index=range(len(percentage_change['bajaj_change'])))
roll_avg['bajaj_rolling_avg']=percentage_change['bajaj_change'].rolling(7).std()
roll_avg=roll_avg.dropna()
roll_avg.plot(kind='line')
plt.show()

###############################################################################

#loading nifty50 
nifty=pd.read_csv("Nifty50.csv") 
#dataframe consisting of close price of nifty
nifty_close_price=pd.DataFrame(index=range(len(nifty['Close'])))
nifty_close_price['nifty_close']=nifty[['Close']]
#dataframe consist of percentage change in close price
nifty_percentage_change=pd.DataFrame(index=range(len(nifty['Close'])))
nifty_percentage_change['nifty_change']=nifty_close_price['nifty_close'].pct_change()
#dropping NAN values
nifty_percentage_change=nifty_percentage_change.dropna()
#dataframe consist of nifty 7 day rolling average
nifty_roll_avg=pd.DataFrame(index=range(len(nifty_percentage_change['nifty_change'])))
nifty_roll_avg['nifty_rolling_avg']=nifty_percentage_change['nifty_change'].rolling(7).std()
nifty_roll_avg=nifty_roll_avg.dropna()
#dataframe for nifty and bajaj finance 7 day rolling average
rolling_avg=pd.DataFrame(index=range(len(nifty_roll_avg['nifty_rolling_avg'])))
rolling_avg['bajaj']=roll_avg[['bajaj_rolling_avg']]
rolling_avg['nifty']=nifty_roll_avg[['nifty_rolling_avg']]
#plotting dataframe
rolling_avg.plot(kind='line')
plt.show()

###############################################################################
     
#dataframe for moving averages
moving_averages=pd.DataFrame(index=range(len(bajfinance['Close Price'])))
#calculating 21 DMA
moving_averages['DMA21']=bajfinance['Close Price'].rolling(21).mean()
#calculating 34 DMA
moving_averages['DMA34']=bajfinance['Close Price'].rolling(34).mean()
moving_averages['bajaj']=bajfinance['Close Price']
moving_averages=moving_averages.dropna()
# Create signals
moving_averages['signal']=0.0
moving_averages['signal'][21:] = np.where(moving_averages['DMA21'][21:] > moving_averages['DMA34'][21:], 1.0, 0.0)   
# Generate trading orders
moving_averages['positions'] = moving_averages['signal'].diff()
# Initialize the plot figure
fig = plt.figure()
# Add a subplot and label for y-axis
ax1 = fig.add_subplot(111,  ylabel='Price in $')
# Plot the closing price
bajfinance['Close Price'].plot(ax=ax1, color='g', lw=2.)
# PlotTING 21 DMA AND34DMA
moving_averages[['DMA21', 'DMA34']].plot(ax=ax1, lw=2.)
# Plot the buy signals
ax1.plot(moving_averages.loc[moving_averages.positions == 1.0].index, moving_averages.DMA21[moving_averages.positions == 1.0],'^', markersize=10, color='m')
# Plot the sell signals
ax1.plot(moving_averages.loc[moving_averages.positions == -1.0].index, moving_averages.DMA21[moving_averages.positions == -1.0],'v', markersize=10, color='k')
# Show the plot
plt.show()

###############################################################################

#dataframe for upper band,lower band and close price
bollinger=pd.DataFrame(index=range(len(bajfinance['Close Price'])))
bollinger['middle_band']=bajfinance['Close Price'].rolling(14).mean()
#calculating 14 day mean and standard deviation
sma=bajfinance['Close Price'].rolling(14).mean()
rstd=bajfinance['Close Price'].rolling(14).std()
bollinger['price']=bajfinance['Close Price']
#calculating upper and lower bollinger bands
bollinger['upper_band'] = sma + 2 * rstd
bollinger['lower_band'] = sma - 2 * rstd
#plotting the graph
bg=bollinger.plot(kind='line')
bg.fill_between(bollinger.index, bollinger['lower_band'], bollinger['upper_band'], color='#ADCCFF', alpha='0.4')
plt.show()




# In[ ]:




# In[ ]:



