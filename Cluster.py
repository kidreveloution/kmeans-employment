import pandas as pd
from sklearn.cluster import KMeans
from tkinter import *
from tkinter import filedialog as fd


#Grab the cluster file
df = pd.read_csv("cluster.csv")


#Importing the files internally with only the important variables
identifier = "Location ID"
lat = "Latitude"
long = "Longitude"
maxClusters = 150

#Final File
X=df.loc[:,[identifier,lat,long]]


#Total Amount of clusters below
numClusters = 150

#Kmeans algorithm with init
kmeans = KMeans(numClusters, init ='k-means++')
#Adding in the cluster label for the points to add
X['cluster_label'] = kmeans.fit_predict(X[X.columns[1:10]])

#Grabbing the centers of the clusters
centers = kmeans.cluster_centers_ #We'll go ahead and use these centers to find out optimal zipcodes later

newdf = pd.DataFrame(X)

print(newdf)

newdf.to_csv('ProcessedFile.csv')
#print(labels)
#print(centers)

