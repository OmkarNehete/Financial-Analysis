import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.formula.api import ols
import statsmodels.api as sm


###############################################################################
#PROBLEM STATEMENT 3.1
#loading the dataset of gold
df1=pd.read_csv("GOLD.csv") 
gold=df1.copy()


###############################################################################
#PROBLEM STATEMENT 3.2
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
plt.show()
#printing monthly beta which is slope1
print('Daily beta of HDFC stock is =',slope1)
####################################################################
####################################################################
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
plt.show()
#printing monthly beta which is slope2
print('Monthly beta of HDFC stock is =',slope2)

###############################################################################























