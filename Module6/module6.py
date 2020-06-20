import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer

###############################################################################

##PROBLEM STATEMENT 6.1

##creating dataframe of closing prices of 30 stocks of all 3 caps
#loading the closing prices of all the stocks 
closing_prices=pd.DataFrame()

adanipower=pd.read_csv("ADANIPOWER.csv")
closing_prices['adanipower']=adanipower['Close Price']

apollotyre=pd.read_csv("APOLLOTYRE.csv")
closing_prices['apollotyre']=apollotyre['Close Price']

asianpaint=pd.read_csv("ASIANPAINT.csv")
closing_prices['asianpaint']=asianpaint['Close Price']

axisbank=pd.read_csv("AXISBANK.csv")
closing_prices['axisbank']=axisbank['Close Price']

bajfinance=pd.read_csv("BAJFINANCE.csv")
closing_prices['bajfinance']=bajfinance['Close Price']

bomdyeing=pd.read_csv("BOMDYEING.csv")
closing_prices['bomdyeing']=bomdyeing['Close Price']

centuryply=pd.read_csv("CENTURYPLY.csv")
closing_prices['centuryply']=centuryply['Close Price']

godrej=pd.read_csv("GODREJIND.csv")
closing_prices['godrej']=godrej['Close Price']

hdfcbank=pd.read_csv("HDFCBANK.csv")
closing_prices['hdfcbank']=hdfcbank['Close Price']

hero=pd.read_csv("HEROMOTOCO.csv")
closing_prices['hero']=hero['Close Price']

idfc=pd.read_csv("IDFC.csv")
closing_prices['idfc']=idfc['Close Price']

infy=pd.read_csv("INFY.csv")
closing_prices['infy']=infy['Close Price']

jetairways=pd.read_csv("JETAIRWAYS.csv")
closing_prices['jetairways']=jetairways['Close Price']

jindalsteel=pd.read_csv("JINDALSTEL.csv")
closing_prices['jindalsteel']=jindalsteel['Close Price']

jubfood=pd.read_csv("JUBlFOOD.csv")
closing_prices['jubfood']=jubfood['Close Price']

lalpathlab=pd.read_csv("LALPATHLAB.csv")
closing_prices['lalpathlab']=lalpathlab['Close Price']

lemontree=pd.read_csv("LEMONTREE.csv")
closing_prices['lemontree']=lemontree['Close Price']

lt=pd.read_csv("LT.csv")
closing_prices['lt']=lt['Close Price']

mindtree=pd.read_csv("MINDTREE.csv")
closing_prices['mindtree']=mindtree['Close Price']

raymond=pd.read_csv("RAYMOND.csv")
closing_prices['raymond']=raymond['Close Price']

reliance=pd.read_csv("RELIANCE.csv")
closing_prices['reliance']=reliance['Close Price']

relinfra=pd.read_csv("RELINFRA.csv")
closing_prices['relinfra']=relinfra['Close Price']

sonata=pd.read_csv("SONATSOFTW.csv")
closing_prices['adanipower']=adanipower['Close Price']

suntv=pd.read_csv("SUNTV.csv")
closing_prices['suntv']=suntv['Close Price']

tatapower=pd.read_csv("TATAPOWER.csv")
closing_prices['tatapower']=tatapower['Close Price']

tcs=pd.read_csv("TCS.csv")
closing_prices['tcs']=tcs['Close Price']

titan=pd.read_csv("TITAN.csv")
closing_prices['titan']=titan['Close Price']

venkeys=pd.read_csv("VENKEYS.csv")
closing_prices['venkeys']=venkeys['Close Price']

voltas=pd.read_csv("VOLTAS.csv")
closing_prices['voltas']=voltas['Close Price']

welspunind=pd.read_csv("WELSPUNIND.csv")
closing_prices['welspunind']=welspunind['Close Price']

###############################################################################

##PROBLEM STATEMENT 6.2
#calculating annual percent returns of the stocks
annual_change=pd.DataFrame()
daily_change=closing_prices.pct_change() 
daily_change=daily_change.dropna()
annual_change=daily_change.sum()

#calculating annual mean deviation of daily percentage change of every stock
annual_mean_volatilities=pd.DataFrame()
annual_mean_volatilities=daily_change.rolling(7).std() 
annual_mean_volatilities=annual_mean_volatilities.dropna()
annual_mean_volatilities=annual_mean_volatilities.sum()

###############################################################################

##PROBLEM STATEMENT 6.3
##creating dataframe of annual percent change and annual mean volatilities
df=pd.DataFrame()
frames=[annual_change,annual_mean_volatilities]
df=pd.concat(frames,axis=1)
df.columns=['annual_change','annual_mean_volatilities']

# Instantiate a scikit-learn K-Means model
model = KMeans(random_state=0)
  
#finding theoptiml cluster values for clustering 
# Instantiate the KElbowVisualizer with the number of clusters and the metric 
visualizer = KElbowVisualizer(model, k=(2,25), metric='silhouette', timings=False)

# Fit the data and visualize
visualizer.fit(df)    
visualizer.poof() 

###############################################################################

##PROBLEM STATEMENT 6.4
# Specify the number of clusters (3) and fit the data X
kmeans = KMeans(n_clusters=3, random_state=0).fit(df)

#plotting the clusters and annonating the points 
#ax=plt.scatter(df.iloc[:,0], df.iloc[:,1], c=kmeans.labels_.astype(float))
ax = df.plot('annual_change', 'annual_mean_volatilities', kind='scatter', s=20 , c=kmeans.labels_.astype(float))
for k, v in df.iterrows():
    ax.annotate(k, v)
plt.show()

###############################################################################




























