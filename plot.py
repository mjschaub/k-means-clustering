import os
from urllib import request
import numpy as np
from KM import KM
import pickle 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
IRIS="iris.txt"
IRIS_URL="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

if not os.path.exists(IRIS):
	raw =request.urlopen(IRIS_URL).read().decode('utf-8')
	with open(IRIS,"w") as f:
		f.write(raw)
data=[]
label=[]
with open(IRIS,"r") as f:
	for line in f:
		temp=line.rstrip()
		if temp!="":
			temp=temp.split(",")
			data.append([float(temp[i]) for i in range(len(temp)-1)])
			label.append(temp[-1])

#PART A:
"""
best_cluster="best_cluster(3,5).p"
kms=[KM(3,5) for i in range(4)]
ss=[]
for km in kms:
	km.cluster(data)
	print("number of clusters:",len(km.clusters))
	ss.append(km.ss_total(data))
print("ss_total:",ss)
with open(best_cluster,"wb") as f:
	pickle.dump(kms[np.argmin(ss)].clusters,f)
"""

#PART B:

best_cluster="best_cluster(3,5).p"
with open(best_cluster,"rb") as f:
	clustering=pickle.load(f)

"""
# find the number of each category:
num={"Iris-setosa":0,"Iris-versicolor":0,"Iris-virginica":0}
for iris in label:
	num[iris]+=1
distribution=[{"Iris-setosa":0,"Iris-versicolor":0,"Iris-virginica":0} for i in range(len(clustering))]
for i in range(len(clustering)):
	for idx in clustering[i][1]:
		distribution[i][label[idx]]+=1
print(distribution)
# pick three distnct clusters
#compute the F1 scores:
F1_scores={}
for key,value in num.items():
	temp=distribution[0]
	for cluster in distribution:
		if cluster[key]>temp[key]:
			temp=cluster
	distribution.remove(temp)
	sizeOfCluster=0
	for name,sample_num in temp.items():
		sizeOfCluster+=sample_num
	Recall=temp[key]/value
	Precision=temp[key]/sizeOfCluster
	F1_scores[key]=2*Precision*Recall/(Precision+Recall)
print(distribution)
avgF1=0
for key,value in F1_scores.items():
	avgF1+=value*num[key]/len(label)
F1_scores["average"]=avgF1
for key,value in F1_scores.items():
	#print(key,":",value)
	print(key,":","%.2f" % round(value,2))
"""

# draw graphs of the best clustering:
fig = plt.figure(4, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
centroids=[]
Y=[]
X=[]
color=0
colors=["purple","red","cyan"]
a1=1
a2=2
a3=3
for cluster in clustering:
	centroids.append(cluster[0])
	for idx in cluster[1]:
		X.append(data[idx])
		Y.append(colors[color])
	ax.scatter([cluster[0][a1]],[cluster[0][a2]],[cluster[0][a3]],c=colors[color],marker='*',s=[200])
	color+=1
X=np.array(X)


ax.scatter(X[:, a1], X[:, a2], X[:, a3], c=Y,
           cmap=plt.cm.Paired)

attribs=["Sepal Length","Sepal Width","Petal Length","Petal Width"]
ax.set_title("Best Clustering:")
ax.set_xlabel(attribs[a1])
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel(attribs[a2])
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel(attribs[a3])
ax.w_zaxis.set_ticklabels([])

plt.show()
