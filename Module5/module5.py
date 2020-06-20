import pandas as pd
import matplotlib.pyplot as plt 
from math import sqrt
import numpy as np
import seaborn as sns

###############################################################################

##PROBLEM STATEMENT 5.1
#importing hdfc stock
hdfc=pd.read_csv("HDFC.csv")
#creating a copy of original dataframe
hdfc=hdfc.copy()
#deleting rows in 'Series' column where value is other than EQ
hdfc.drop(hdfc[hdfc.Series != 'EQ'].index , inplace=True)
#calculating daily percentage change of hdfc stock
hdfc['Day_Perc_Change']=hdfc['Close Price'].pct_change() 
#calculating annual mean of daily percentage change of hdfc stock
hdfc['annual_mean']=hdfc['Day_Perc_Change'].rolling(7).mean() * 252
#calculating annual standard deviation of daily percentage change of hdfc stock
hdfc['annual_std']=hdfc['Day_Perc_Change'].rolling(7).std() * sqrt(252)
#dropping rows with NAN values
hdfc=hdfc.dropna()
#plotting anual standard deviation as line graph
hdfc['annual_std'].plot(kind='line')
plt.show()

###############################################################################

#PROBLEM STATEMENT 5.2
#importing reliance stock
reliance=pd.read_csv("RELIANCE.csv")
#importing bajfinance stock
bajaj=pd.read_csv("BAJFINANCE.csv")
 #importing tcs stock
tcs=pd.read_csv("TCS.csv")
#importing lt stock
lt=pd.read_csv("LT.csv")
#importing titan stock
titan=pd.read_csv("TITAN.csv")
#calculating daily percent change of every stock
reliance['Day_Perc_Change']=reliance['Close Price'].pct_change() 
bajaj['Day_Perc_Change']=bajaj['Close Price'].pct_change() 
tcs['Day_Perc_Change']=tcs['Close Price'].pct_change() 
lt['Day_Perc_Change']=lt['Close Price'].pct_change() 
titan['Day_Perc_Change']=titan['Close Price'].pct_change() 

#calculating annual mean of daily percentage change of every stock
reliance['annual_mean']=reliance['Day_Perc_Change'].rolling(7).mean() * 252
bajaj['annual_mean']=bajaj['Day_Perc_Change'].rolling(7).mean() * 252
tcs['annual_mean']=tcs['Day_Perc_Change'].rolling(7).mean() * 252
lt['annual_mean']=lt['Day_Perc_Change'].rolling(7).mean() * 252
titan['annual_mean']=titan['Day_Perc_Change'].rolling(7).mean() * 252

#calculating annual standard deviation of daily percentage change of every stock
reliance['annual_std']=reliance['Day_Perc_Change'].rolling(7).std() * sqrt(252)
bajaj['annual_std']=bajaj['Day_Perc_Change'].rolling(7).std() * sqrt(252)
tcs['annual_std']=tcs['Day_Perc_Change'].rolling(7).std() * sqrt(252)
lt['annual_std']=lt['Day_Perc_Change'].rolling(7).std() * sqrt(252)
titan['annual_std']=titan['Day_Perc_Change'].rolling(7).std() * sqrt(252)

#creating new dataframe for closing prices of all the stocks
day_change=pd.DataFrame(index=range(len(tcs)))
day_change['reliance']=reliance['Close Price'].pct_change()
day_change['bajaj']=bajaj['Close Price'].pct_change() 
day_change['tcs']=tcs['Close Price'].pct_change() 
day_change['lt']=lt['Close Price'].pct_change() 
day_change['titan']=titan['Close Price'].pct_change() 

#dropping rows with NAN values 
day_change=day_change.dropna()
annual_return=day_change.mean()*252

#creating new dataframe for closing prices of all the stocks
close=pd.DataFrame(index=range(len(tcs)))
close['reliance']=reliance['Close Price']
close['bajaj']=bajaj['Close Price']
close['tcs']=tcs['Close Price']
close['lt']=lt['Close Price']
close['titan']=titan['Close Price']
#dropping NAN values
close=close.dropna()

#equal weights as given in the problem statement
weights=np.array([0.2,0.2,0.2,0.2,0.2])
#calculating annual returns of the portfolio
portfolio_return=np.dot(weights,annual_return)
#calculating covariance of the portfolio
portfolio_cov=day_change.cov()*252
#calculating risk/volatility of the portfolio
portfolio_risk=np.dot(weights.T,np.dot(portfolio_cov,weights))**0.5
##calculating sharpe ratio for the portfolio
SharpeRatio=portfolio_return/portfolio_risk
#printing sharpe ratio
print('Sharpe ratio of the selected portfolio is',SharpeRatio)

###############################################################################
#PROBLEM STATEMENT 5.3
#plotting the scatter plot of for 1000 portfolios 
#creating lists for returns,volatility,sharpe ratio and coins 
pf_returns,pf_volatility,pf_sharpe_ratio,pf_coins=([] for i in range(4))
#created 1000 portfolios
num_portfolios=10000
#iterating through each portfolio
for portfolio in range(num_portfolios):
    #random weights
    weights=np.random.random(5)
    weights/=np.sum(weights)
    #returns for portfolio
    returns=np.dot(weights,annual_return)
    #volatility of the portfolio
    volatility=np.dot(weights.T,np.dot(portfolio_cov,weights))**0.5
    #sharpe ratio of the portfolio
    sharpe_ratio=returns/volatility
    #appending each parameter
    pf_coins.append(weights)
    pf_returns.append(returns)
    pf_volatility.append(volatility)
    pf_sharpe_ratio.append(sharpe_ratio)
#plotting the scatter plot 
x=max(pf_returns)
y=min(pf_volatility)
plt.figure(figsize=(12,8))
plt.scatter(x=pf_volatility,y=pf_returns,c=pf_sharpe_ratio,cmap='viridis',s=15)
plt.colorbar(label='Sharpe Ratio')
sns.set(style='darkgrid')
plt.xlabel('Volatility')
plt.ylabel('Returns')
plt.show()

###############################################################################
###PROBLEM STATEMENT 5.4
#marking the portfolio with highest volatility and lowest returns
df=pd.DataFrame(index=range(len(pf_returns)))
df['pf_returns']=pf_returns
df['pf_volatility']=pf_volatility
#max value of pf_returns
x1=df['pf_returns'].max()
#corresponding value of returns
for i,j in df.iterrows():
    if df['pf_returns'][i] == x1:
        y1=df['pf_volatility'][i]
#min value of pf_volatility    
x2=df['pf_volatility'].min()
#corresponding of volatility
for k,l in df.iterrows():
    if df['pf_volatility'][k] == x2:
        y2=df['pf_returns'][k]
x=[x1,y1]
y=[x2,y2]
#plotting the values
plt.figure(figsize=(10,6))
plt.scatter(x=y,y=x,marker='*',s=30)
plt.show()
###############################################################################










