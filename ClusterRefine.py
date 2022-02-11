import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import math
import operator

df = pd.read_csv('clusterFile.csv')

X=df.loc[:,['Location ID','Latitude','Longitude','cluster_label']]
print(X)
y=0
i = 0
for i in range(0,len(X)):
    maxVofC = X['cluster_label'].max()
    counter = len(X[X.cluster_label.eq(i)])
    if counter > 10:
        divider = (math.ceil(counter/2))
        print("The divider is",divider)
        defy = X[X.cluster_label.eq(i)]
        print("The Length of this is",len(defy))
        index_list = list(defy.index.values)
        halfindex = math.ceil(len(index_list)/2)
        cNum = X.loc[index_list[1], 'cluster_label']
        print(cNum)
        for y in range(0,halfindex):
            X.loc[index_list[y], 'cluster_label'] = maxVofC + 1


print(X)
print("Maximum",maxVofC)
X.to_csv('RefinedCSV.csv', mode='a', header=True , index = False)



