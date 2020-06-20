import pandas as pd

###############################################################################
#PROBLEM STATEMENT 1.1
#importing csv file
dforg=pd.read_csv("HDFC.csv") 
dforg=pd.DataFrame(dforg)
df=dforg.copy()
#deleting rows in 'Series' column where value is other than EQ
df.drop(df[df.Series != 'EQ'].index , inplace=True)
#performing some functions on the dataframe
print(df.head())
print(df.tail())
print(df.describe())
print(df.shape)
###############################################################################

#PROBLEM STATEMENT 1.2
#getting rows for last 90 days
df90=df.tail(90)
#printing minimum,maximum and mean closing prices
print('Maximum closing price of last 90 days is',df90['Close Price'].max())
print('Minimum closing price of last 90 days is',df90['Close Price'].min())
print('Mean closing price of the last 90 days is',df90['Close Price'].mean())
###############################################################################

#PROBLEM STATEMENT 1.3
#datatypes of each column
print('datatypes of the columns are as follows ',df.dtypes)
#changing date column from object format to datetime format
df['Date'] = pd.to_datetime(df['Date'])
print('datatype of Date column is ',df['Date'].dtypes)
#subtracting minimum date valur from maximum date value
result=df['Date'].max() - df['Date'].min()
print('result of subtraction of dates is ',result)
###############################################################################

#PROBLEM STATEMENT 1.4
#creating month and year dataframes
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
#applying groupby() to month and year
dfVWAP = df.groupby(['Year','Month']).first()
#calculating VWAP for every month
dfVWAP['VWAP']=dfVWAP['Close Price']*dfVWAP['Total Traded Quantity'].groupby(['Year','Month']).sum()/dfVWAP['Total Traded Quantity'].groupby(['Year','Month']).sum()
dfVWAP.to_csv('VWAP_month.csv') 
###############################################################################

#PROBLEM STATEMENT 1.5
#calculating average price over last N days
def average_price():
    n=int(input('enter number of days to calculate average stock price '))
    dfaverage=df.tail(n)
    print('average price of the stock in the past '+str(n)+ ' days is',dfaverage['Average Price'].sum()/n)
average_price()  

#calculating profit/loss percentage
def pnl():
    m=int(input('enter number of days to calculate average stock price'))
    dfpnl=df.tail(m)
    #calculating percentage change
    dfpnl['Day_Perc_Change']=dfpnl['Close Price'].pct_change()*100 
    #setting first NAN value to 0
    dfpnl['Day_Perc_Change'].iloc[0]=0
    print(dfpnl)    
pnl()
###############################################################################

#PROBLEM STATEMENT 1.6
#calculating percentage change
df['Day_Perc_Change']=df['Close Price'].pct_change()*100 
#setting first NAN value to 0
df['Day_Perc_Change'].iloc[0]=0
###############################################################################

#PROBLEM STATEMENT 1.7
#adding column 'Trend' in the dataframe
df['Trend']=''
#values to be inserted
insert_value=['Slight or No change','Slight positive','Slight negative','Positive','Negative','Among top gainers','Among top losers','Bull run','Bear drop']
#iterating through the dataframe 
for index,row in df['Day_Perc_Change'].iteritems():
    if row > -0.5 and row < 0.5 :
        df['Trend'][index]=insert_value[0]
    elif row > 0.5 and row < 1:
        df['Trend'][index]=insert_value[1]
    elif row > -1 and row < -0.5:
        df['Trend'][index]=insert_value[2]
    elif row > 1 and row < 3:
        df['Trend'][index]=insert_value[3]
    elif row > -3 and row < -1:
        df['Trend'][index]=insert_value[4]
    elif row > 3 and row < 7:
        df['Trend'][index]=insert_value[5]
    elif row > -7 and row < -3:
        df['Trend'][index]=insert_value[6]
    elif row > 7:
        df['Trend'][index]=insert_value[7]
    elif row < -7:
        df['Trend'][index]=insert_value[8]   
###############################################################################

#PROBLEM STATEMENT 1.8
#grouping Trend column
dftrend = df[['Total Traded Quantity','Trend']]
d=dftrend.groupby(dftrend['Trend']).mean()
#dftrend=dftrend.groupby(dftrend['Trend']).median()
print(d)
#dftrend['Median Traded Quantity']=dftrend.groupby('Trend').median()
dftrend.to_csv('Trend.csv') 
###############################################################################

# saving the dataframe 
df.to_csv('week2.csv') 