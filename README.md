# kmeans-employment
A program that helps employers figure out how many employees they need based on store clustering using the K Means algorithm. 

How does this work? 

1) Start @ Cluster.py
    a) 'cluster.csv' (included), is a list of all BestBuy's in the United States.
        Cluster.py will take all this geographic data, plot it, and cluster all the 
        nodes based on the number of clusters you want. 

2) Refine the cluster with ClusterRefine.py
    a) K-means is not perfect, and can often cluster too many nodes together. (Too many stores
       clumped up in the New York Area). This script will continue splitting up nodes lattitude
       or longitude wise depending on the max amount of nodes in a cluster

       1) This can be improved. Instead of simply splitting the clusters, re-run K-means within 
          the larger cluster for better results

So What are the other files?

As I continue to implement a frontend, along with API's and what not, I will continue devoloping 
when I can. 

elbowClusters.py for example, is a script that given all the clusters, will return the optimal amount
of clusters (The idea that most clusters should equal the same size)


