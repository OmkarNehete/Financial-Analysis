import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns

###############################################################################
#PROBLEM STATEMENT 3.1
#loading the dataset of gold
df1=pd.read_csv("GOLD.csv") 
gold=df1.copy()
#dropping NAN values
gold=gold.dropna()
#setting x and y values for linear regression
X=gold['Pred'].values.reshape(-1,1)
Y=gold['new'].values.reshape(-1,1)
#saving LinearRegression() in reg variable
reg=LinearRegression()
#performing linear regression 
reg.fit(X,Y)
#predicting the x values which are empty in the dataframe
predictions=reg.predict(X)
#printing the predicted values
print(predictions)
#plotting the regression values as scatter plot
plt.plot(gold['Pred'],gold['new'],'b.')
#plotting regression line
plt.plot(gold['Pred'],predictions,c='red',linewidth=2)
plt.xlabel("Pred")
plt.ylabel("new")
plt.grid(True)
plt.show()
#plotting histogram of Pred column
x=gold['Pred']
plt.hist(x, bins=30,color='red')
plt.show()
# Density Plot and Histogram of Pred column
sns.distplot(gold['Pred'],  kde=True, color = 'orange' )
plt.show()

###############################################################################

#PROBLEM STATEMENT 3.2
#CALCULATING DAILY BETA VALUE
#loading the dataset of HDFC stock
df2=pd.read_csv("HDFC.csv") 
hdfc=df2.copy()
#loading the dataset of NIFTY
df3=pd.read_csv("Nifty50.csv") 
nifty=df3.copy()
#deleting rows in 'Series' column where value is other than EQ
hdfc.drop(hdfc[hdfc.Series != 'EQ'].index , inplace=True)
#getting rows for last 90 days that is 3 months for nifty50 index
nifty90=nifty.tail(90)
#getting rows for last 90 days that is 3 months for HDFC stock
hdfc90=hdfc.tail(90)
#calculating daily percentage change of hdfc stock
hdfc90['Day_Perc_Change']=hdfc90['Close Price'].pct_change()*100 
#setting first NAN value to 0
hdfc90['Day_Perc_Change'].iloc[0]=0
#calculating daily percentage change of Nifty50 index
nifty90['Day_Perc_Change']=nifty90['Close'].pct_change()*100
#setting first NAN value to 0
nifty90['Day_Perc_Change'].iloc[0]=0
#performing linear regression 
slope1,intercept1,r,p,std_err = stats.linregress(nifty90['Day_Perc_Change'],hdfc90['Day_Perc_Change'])
#daily return of the Nifty50 index
x1=np.linspace(np.amin(nifty90['Day_Perc_Change']),np.amax(nifty90['Day_Perc_Change']))
#daily return of hdfc stock
y1=slope1*x1+intercept1
#plotting the returns
plt.plot(nifty90['Day_Perc_Change'],hdfc90['Day_Perc_Change'],'b.')
plt.grid(True)
#plotting regression line
plt.plot(x1,y1,'r')
plt.xlabel("Nifty50")
plt.ylabel("HDFC")
plt.show()
#printing monthly beta which is slope1
print('Daily beta of HDFC stock is =',slope1)
###############################################################################
###############################################################################
#CALCULATING MONTHLY BETA VALUE
#calculating monthly percentage change of hdfc stock
hdfc['Month_Perc_Change']=hdfc['Close Price'].pct_change(30)*100 
#dropping NAN values
hdfc=hdfc.dropna()
#calculating monthly percentage change of Nifty50 index
nifty['Month_Perc_Change']=nifty['Close'].pct_change(30)*100
#dropping NAN values
nifty=nifty.dropna()
#performing linear regression 
slope2,intercept2,r,p,std_err = stats.linregress(nifty['Month_Perc_Change'],hdfc['Month_Perc_Change'])
#daily return of the Nifty50 index
x2=np.linspace(np.amin(nifty['Month_Perc_Change']),np.amax(nifty['Month_Perc_Change']))
#daily return of hdfc stock
y2=slope2*x2+intercept2
#plotting the returns
plt.plot(nifty['Month_Perc_Change'],hdfc['Month_Perc_Change'],'b.')
plt.grid(True)
#plotting regression line
plt.plot(x2,y2,'r')
plt.xlabel("Nifty50")
plt.ylabel("HDFC")
plt.show()
#printing monthly beta which is slope2
print('Monthly beta of HDFC stock is =',slope2)

###############################################################################

"""
*****BRIEF ABOUT THE BETA VALUES AND THE REGRESSION GRAPHS*****

BETA DEFINITION:
    Beta is a measure of a stock's volatility in relation to the market. 
By definition, the market has a beta of 1.0, and individual stocks are ranked according to how much they deviate from the market. 
A stock that swings more than the market over time has a beta above 1.0. 
If a stock moves less than the market, the stock's beta is less than 1.0. 
High-beta stocks are supposed to be riskier but provide a potential for higher returns; low-beta stocks pose less risk but also lower returns.
    Beta is a key component for the capital asset pricing model (CAPM), which is used to calculate the cost of equity. 
Recall that the cost of capital represents the discount rate used to arrive at the present value of a company's future cash flows. 
All things being equal, the higher a company's beta is, the higher its cost of the capital discount rate. 
The higher the discount rate, the lower the present value placed on the company's future cash flows. In short, beta can impact a company's

**Daily beta values for the stock is 1.12 which is greater than 1, which means that the stock is more risky but also gives more returns on a daily basis.
**Monthly beta values for the stock is 0.909 which is less than 1, which means that the stock is less risky but  also gives less returns on a monthly basis .
**Negative beta indicates that the stock is performing better even when the market is falling.
**This is very unliklely situation as the stock will however follow the market trend now or sometime later.

REGRESSION ANALYSIS:
**By regression graphs we can observe that the slope of the line is positive which means that the beta is positive.
**Daily plot values of Nifty50 and HDFC stock lies between -0.5 and 0.5.
**Monthlyl plot values of Nifty50 and HDFC stock lies between -0.25 and 5.
**Regression lines show the most likely trend which the entity can follow. Here our entity is a stock.
**The line follows the concept of gradient descent which basically means that the line will be drawn such that the distance betwwen all the points and the line will be as less as possible.
**Here the regression lines for both daily and monthly timeframe shows a positive trend which means that the stock will likely give postive returns in the coming future.

"""















