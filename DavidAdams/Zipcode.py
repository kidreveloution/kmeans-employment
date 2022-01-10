import geopy
import pandas as pd
import numpy as np
import csv

df = pd.read_csv('RFP Coverage - Working Copy.csv')
i = 0
X=df.loc[:,['Name','Latitude','Longitude','ClusterAssigned']]
index_list = list(X.index.values)
cordList = []
clumList = []
zipLats = []
zipLons = []

for i in range (1,126):
    filter = X[X.ClusterAssigned.eq(i)]
    filter = filter.reset_index(drop=True)
    index_list = list(filter.index.values)
    #print(len(filter))
    #print(filter)
    latMean = filter['Latitude'].sum()/len(filter)
    lonMean = filter['Longitude'].sum()/len(filter)
    #print(latMean)
    #print(lonMean)
    cordList.append([latMean,lonMean])
    clusterNum = filter.loc[0, "ClusterAssigned"]
    clumList.append(clusterNum)

print(cordList)

with open('zipcode.csv', "w") as f:
    writer = csv.writer(f)
    for row in cordList:
        writer.writerow(row)

