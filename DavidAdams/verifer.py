import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import math

df = pd.read_csv('ender1.csv')

X=df.loc[:,['Location ID','Latitude','Longitude','cluster_label']]
counter = len(df.cluster_label == 5)


for i in range(0,len(X)):
    counter = len(X[X.cluster_label.eq(i)])
    print(counter)