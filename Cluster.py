import pandas as pd
from sklearn.cluster import KMeans
from tkinter import *
from tkinter import filedialog as fd

#filename = fd.askopenfilename()


df = pd.read_csv("cluster.csv")

identifier = "Location ID"
lat = "Latitude"
long = "Longitude"
maxClusters = 150

#print(df.head)
X=df.loc[:,[identifier,lat,long]]
#K_clusters = range(1,maxClusters+1)
#kmeans = [KMeans(n_clusters=i) for i in K_clusters]
#Y_axis = df[['Latitude']]
#X_axis = df[['Longitude']]
#score = [kmeans[i].fit(Y_axis).score(Y_axis) for i in range(len(kmeans))]


numClusters = 150
kmeans = KMeans(numClusters, init ='k-means++')
X['cluster_label'] = kmeans.fit_predict(X[X.columns[1:10]])
centers = kmeans.cluster_centers_
labels = kmeans.predict(X[X.columns[1:3]])
newdf = pd.DataFrame(X)

print(newdf)
print(labels)
print(centers)

