import pandas as pd
import numpy as np
ds=pd.read_csv('AQI_Data.csv')
#dislay first 8 rows
print("first 8 rows of datset:")
print(ds.head(8))
print()
#display last 5 rows
print("last 5 rows of dataset:")
print(ds.tail(5))
print()
# display dtypes and non null values of each column
print("dtype and number of non-null values in each column")
print(ds.info())
print()
city=ds['City'].to_numpy()
pm25=ds['PM2.5'].to_numpy()
pm10=ds['PM10'].to_numpy()
d={}
aqi=ds['AQI'].to_numpy()
# display mean aqi,max pm2.5,min pm10 using numpy
print("mean aqi of dataset :",np.mean(aqi))
print("maximum pm2.5 of dataset :",np.max(pm25))
print("minimum pm10 of datset",np.min(pm10))
print()
#dislay number of rows for each unique city as dictionary
for i in city:
    if(i not in d):
        d[i]=0
    else:
        d[i]+=1     
print("number of rows per particular city:")
print(d)  
print() 
#computing pollutant concentartions using numpy     
no2=ds['NO2'].to_numpy()
co=ds['CO'].to_numpy()
so2=ds['SO2'].to_numpy()
o3=ds['O3'].to_numpy()
pollsum=pm25+pm10+no2+co+so2+o3
#adding new column to daatset and saving to polltutant .txt
ds['pollutantsum']=pollsum
print("dataset with new column sum of all pollutant is:")
print(ds)
f=open('pollutant.txt','w+')
numds=ds.to_numpy()
l=['City','Date','AQI','PM2.5','PM10','NO2','CO','O3','SO2','Pollutant Sum']
f.write(str(l))
for i in numds:
    f.write(str(i))
f.close()    