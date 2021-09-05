import pandas as pd
from sklearn.cluster import KMeans
from tkinter import *
from tkinter import filedialog as fd

filename = fd.askopenfilename()
print(filename)
window = Tk()


df = pd.read_csv(filename)
data_top = df.head()

col = "not me"

#for col in df.columns:
#    print(col)
colNames = list(df.columns.values)
print (colNames)
window.title("Davids Awesome Program")
window.configure(background = "yellow")
Label (window, text =colNames, bg = "Yellow", fg = "black" ) . grid(row = 1, column = 0, sticky = W)
#outputtext = Text(window)
#outputtext.grid(column=1, row=5)


#print(df.head)
X=df.loc[:,['Location ID','Latitude','Longitude']]
K_clusters = range(1,151)
kmeans = [KMeans(n_clusters=i) for i in K_clusters]
Y_axis = df[['Latitude']]
X_axis = df[['Longitude']]
score = [kmeans[i].fit(Y_axis).score(Y_axis) for i in range(len(kmeans))]
kmeans = KMeans(n_clusters = 150, init ='k-means++')
X['cluster_label'] = kmeans.fit_predict(X[X.columns[1:10]])
centers = kmeans.cluster_centers_
labels = kmeans.predict(X[X.columns[1:3]])
newdf = pd.DataFrame(X)


#newdf.to_csv('clusterFile.csv', mode='a', header=True , index = False)

#print(centers)