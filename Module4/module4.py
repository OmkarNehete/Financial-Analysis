import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier 
from sklearn import metrics 

#################################################################################
##PROBLEM STATEMENT 4.1
##creating call column and training a classification model
#loading the bollinger dataframe which contains upper band,lower band and closing prices of the Bajaj Finance stock
df1=pd.read_csv("bollinger.csv") 
#creating a copy of the original dataframe
bollinger=df1.copy()
#dropping unnamed column
bollinger=bollinger.drop(bollinger.columns[0], axis=1)
#removing NAN values
bollinger=bollinger.dropna()
#creating call column in bollinger dataframe
bollinger['call']=''
#creating calls column in bollinger dataframe
bollinger['calls']=''
#values to be inserted
insert_value=['Buy','Hold Buy/Liquidate Short','Hold Short/Liquidate Buy','Short']
#iterating through the dataframe and inserting appropriate values in call column
for i,j in bollinger.iterrows(): 
    if bollinger['price'][i] < bollinger['lower_band'][i]:
        bollinger['call'][i]=insert_value[0]
    elif bollinger['price'][i]>bollinger['lower_band'][i] and bollinger['price'][i] < bollinger['middle_band'][i]:
        bollinger['call'][i]=insert_value[1]
    elif bollinger['price'][i]>bollinger['middle_band'][i] and bollinger['price'][i] < bollinger['upper_band'][i]:
        bollinger['call'][i]=insert_value[2]
    elif bollinger['price'][i]>bollinger['upper_band'][i]:
        bollinger['call'][i]=insert_value[3] 
#classification of the call column
feature=['middle_band','price','lower_band','upper_band']
#creating x for all the features
X=bollinger[feature]
#creating y for call values to be trained
Y=bollinger.call
# Split dataset into training set and test set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.001, random_state=1)
# Create Decision Tree classifer object
clf = DecisionTreeClassifier()
# Train Decision Tree Classifer
clf = clf.fit(X_train,Y_train)
#Predict the response for test dataset
calls = clf.predict(X)
#merging predicted results with the bollinger dataframe
bollinger['calls']=calls
#printing bollinger datframe
print(bollinger)       
# Model Accuracy
print("Accuracy:",metrics.accuracy_score(Y, calls))
#saving bollinger dataframe
bollinger.to_csv('bollinger.csv') 

########################################
########################################

#importing HDFC stock
df2=pd.read_csv("HDFC.csv")
#creating a copy of the original dataframe
hdfc=df2.copy() 
#deleting rows in 'Series' column where value is other than EQ
hdfc.drop(hdfc[hdfc.Series != 'EQ'].index , inplace=True)
#dataframe for upper band,lower band and close price
bollingerHDFC=pd.DataFrame(index=range(len(hdfc['Close Price'])))
#calculating the middle bollinger band 
bollingerHDFC['middle_band']=hdfc['Close Price'].rolling(14).mean()
#calculating 14 day mean and standard deviation
sma=hdfc['Close Price'].rolling(14).mean()
rstd=hdfc['Close Price'].rolling(14).std()
print(rstd)
#removing NAN values
bollingerHDFC=bollingerHDFC.dropna()
#adding closing price to bollingerHDFC
bollingerHDFC['price']=hdfc['Close Price']
#calculating upper and lower bollinger bands
bollingerHDFC['upper_band'] = sma + 2 * rstd
bollingerHDFC['lower_band'] = sma - 2 * rstd
#plotting the graph
bg=bollingerHDFC.plot(kind='line')
bg.fill_between(bollingerHDFC.index, bollingerHDFC['lower_band'], bollingerHDFC['upper_band'], color='#ADCCFF', alpha='0.4')
plt.show()
#creating call column in bollingerHDFC dataframe
bollingerHDFC['call']=''
#iterating through the dataframe and inserting appropriate values in call column
for i,j in bollingerHDFC.iterrows(): 
    if bollingerHDFC['price'][i] < bollingerHDFC['lower_band'][i]:
        bollingerHDFC['call'][i]=insert_value[0]
    elif bollingerHDFC['price'][i]>bollingerHDFC['lower_band'][i] and bollingerHDFC['price'][i] < bollingerHDFC['middle_band'][i]:
        bollingerHDFC['call'][i]=insert_value[1]
    elif bollingerHDFC['price'][i]>bollingerHDFC['middle_band'][i] and bollingerHDFC['price'][i] < bollingerHDFC['upper_band'][i]:
        bollingerHDFC['call'][i]=insert_value[2]
    elif bollingerHDFC['price'][i]>bollingerHDFC['upper_band'][i]:
        bollingerHDFC['call'][i]=insert_value[3]
#classification of the call column
featureHDFC=['middle_band','price','lower_band','upper_band']
#creating x for all the features
X1=bollingerHDFC[featureHDFC]
#Predict the response for test dataset
calls = clf.predict(X1)
#merging predicted results with the bollinger dataframe
bollingerHDFC['calls']=calls
#printing bollingerHDFC dataframe       
print(bollingerHDFC)
# Model Accuracy
print("Accuracy:",metrics.accuracy_score(bollingerHDFC['call'], calls))
#saving bollingerHDFC dataframe
bollingerHDFC.to_csv('bollingerHDFC.csv') 

###############################################################################

##PROBLEM STATEMENT 4.2

#importing Bajaj Finance stock
df3=pd.read_csv("BAJFINANCE.csv")
#creating a copy of the original dataframe
bajaj=df3.copy() 
#deleting rows in 'Series' column where value is other than EQ
bajaj.drop(bajaj[bajaj.Series != 'EQ'].index , inplace=True)
#dataframe for open and close prices of bajaj stock
open_close=pd.DataFrame(index=range(len(bajaj)))
open_close['Open Price']=bajaj['Open Price']
open_close['Close Price']=bajaj['Close Price']
#calculating percent change of close price per day
bajaj['Day_Perc_Change']= bajaj['Close Price'].pct_change() *100
#adding 4 new columns as per the problem statement
#percent change between open and close price
res1= open_close.pct_change(axis=1,periods=1)*100 
bajaj['Per_Change_OpenandClose']=res1['Close Price']

#dataframe for low and high prices of bajaj stock
high_low=pd.DataFrame(index=range(len(bajaj)))
high_low['Low Price']=bajaj['Low Price']
high_low['High Price']=bajaj['High Price']
#percent change between low and high price
res2= high_low.pct_change(axis=1,periods=1)*100 
bajaj['Per_Change_LowandHigh']=res2['High Price']
#5 day rolling mean of % change of close price
bajaj['Rolling_Mean_5days']=bajaj['Day_Perc_Change'].rolling(5).mean()
#5 day rolling std of % change of close price
bajaj['Rolling_Std_5days']=bajaj['Day_Perc_Change'].rolling(5).std()

####################################
####################################
#dropping NAN values
bajaj=bajaj.dropna()
#creating Action column in bajaj dataframe
bajaj['Action']=''
#iterating through dataframe and inserting appropriate values
for i in range(len(bajaj)):
    j=i+1
    if j < len(bajaj):
        if bajaj['Close Price'].iloc[i] < bajaj['Close Price'].iloc[j]:
            bajaj['Action'].iloc[i] = 1
        elif bajaj['Close Price'].iloc[i] > bajaj['Close Price'].iloc[j]:
            bajaj['Action'].iloc[i] = -1
        elif bajaj['Close Price'].iloc[j]:
            bajaj['Action'].iloc[i] = 0

####################################
####################################

#constructing RandomForest Classifier
#classification of the call column
featurebajaj=['Per_Change_OpenandClose','Per_Change_LowandHigh','Rolling_Mean_5days','Rolling_Std_5days']
#creating x for all the features
X2=bajaj[featurebajaj]
#creating y for call values to be trained
Y2=bajaj.Action
#converting Action column to string datatype
Y2=Y2.astype('str')
# Split dataset into training set and test set
X2_train, X2_test, Y2_train, Y2_test = train_test_split(X2, Y2, test_size=0.001, random_state=1)
# Create Decision Tree classifer object
clf3=RandomForestClassifier(n_estimators=100)
# Train Decision Tree Classifer
clf3 = clf3.fit(X2_train,Y2_train)
#Predict the response for test dataset
Actions = clf3.predict(X2)
#merging predicted results with the bollinger dataframe
bajaj['Actions']=Actions            
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(Y2, Actions))

bajaj['Close Price']=bajaj['Date']
##################################
##################################

#plotting net returns
#calculating cummulative returns of the stock
bajaj['cummulative_returns']=bajaj['Day_Perc_Change'].cumsum()
#plotting cummulative returns of the stock
bajaj.plot(kind='line',y='cummulative_returns')
plt.show()
#saving dataframe of Bajaj Finance with all the new columns
bajaj.to_csv('bajaj.csv') 
     
###############################################################################



 