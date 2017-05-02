
import numpy as np
import ast
import math
import matplotlib.pyplot as plt
import pickle
from mpl_toolkits.mplot3d import Axes3D
#from sklearn.decomposition import PCA



					#https://matplotlib.org/mpl_toolkits/mplot3d/api.html

def euclidean_dist(a,b):
	dist = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2 + (a[3]-b[3])**2)	
	return dist


def change_centroids(clustering,remove_data):

	#print('changing centroids')
	if remove_data is True:
		for i in clustering.keys():
			if clustering[i] == []:
				del clustering[i]
				continue
			new_centroid = [0.0,0.0,0.0,0.0]
			for e in clustering[i]:
				for z in range(len(e)):
					if z == 4:
						break
					new_centroid[z]+=e[z]
		
			new_centroid = [x/len(clustering[i]) for x in new_centroid]
			del clustering[i]
			clustering[repr(new_centroid)] = []
	else:
		for i in clustering.keys():
			if clustering[i] == []:
				del clustering[i]
				continue
			new_centroid = [0.0,0.0,0.0,0.0]
			for e in clustering[i]:
				for z in range(len(e)):
					if z == 4:
						break
					new_centroid[z]+=e[z]
		
			new_centroid = [x/len(clustering[i]) for x in new_centroid]
			clustering[repr(new_centroid)] = clustering[i]
			

def calc_SS_total(clustering):
	total_sum = 0
	for i in clustering.keys():
		for e in clustering[i]:
			total_sum+= euclidean_dist(e[0:4],ast.literal_eval(i))**2
	return total_sum


if __name__ =='__main__':
	
	iris_data = []
	with open('iris.data') as f:
    		content = f.readlines()
	for x in content:
		iris_data.append(x.strip().split(','))
	for x in iris_data:
		for y in range(len(x)):
			if y == 4:
				break
			x[y] = float(x[y])
	complete_ss_totals = []
	three_best_clustering = []
	for j in range(0,3):
		print('doing a k-means run for index: ' ,(j+3))
		SS_totals = []
		best_clustering = []
		for i in range(0,3): # 0 for 5 times, 1 for 10, 2 for 20
			print ('beginning the four cluster attempts for range ', i)
			for b in range(0,4):
				clusters = []
				for t in range(0,j+3):
					clusters.append(np.random.uniform(low=0.0, high=10.0, size=4).tolist())
				curr_clustering = dict()
				for x in clusters:
					curr_clustering[repr(x)] = []
				if i == 0:
					for a in range(0,5):
						for x in iris_data:
							best_centroid = curr_clustering.keys()[0]
							smallest_distance = euclidean_dist(ast.literal_eval(best_centroid),x[0:4])
							for y in curr_clustering.keys():
								curr_dist = euclidean_dist(ast.literal_eval(y),x[0:4])
								if curr_dist < smallest_distance:
									smallest_distance = curr_dist
									best_centroid = y
							curr_clustering[best_centroid].append(x)
						should_remove_data_points = True
						if a == 4:
							should_remove_data_points = False
						change_centroids(curr_clustering,should_remove_data_points)
				elif i == 1:
					for a in range(0,10):
						for x in iris_data:
							best_centroid = curr_clustering.keys()[0]
							smallest_distance = euclidean_dist(ast.literal_eval(best_centroid),x[0:4])
							for y in curr_clustering.keys():
								curr_dist = euclidean_dist(ast.literal_eval(y),x[0:4])
								if curr_dist < smallest_distance:
									smallest_distance = curr_dist
									best_centroid = y
							curr_clustering[best_centroid].append(x)
						should_remove_data_points = True
						if a == 9:
							should_remove_data_points = False
						change_centroids(curr_clustering,should_remove_data_points)
				elif i == 2:
					for a in range(0,20):
						for x in iris_data:
							best_centroid = curr_clustering.keys()[0]
							smallest_distance = euclidean_dist(ast.literal_eval(best_centroid),x[0:4])
							for y in curr_clustering.keys():
								curr_dist = euclidean_dist(ast.literal_eval(y),x[0:4])
								if curr_dist < smallest_distance:
									smallest_distance = curr_dist
									best_centroid = y
							curr_clustering[best_centroid].append(x)
						should_remove_data_points = True
						if a == 19:
							should_remove_data_points = False
						change_centroids(curr_clustering,should_remove_data_points)
				
				SS_totals.append((curr_clustering, calc_SS_total(curr_clustering)))
			
			best_ss = SS_totals[i*4][1]
			best_clustering_to_add = SS_totals[i*4]#[0]
			for z in range(i*4,4*(i+1)):
				if SS_totals[z][1] < best_ss:
					best_ss = SS_totals[z][1]
					best_clustering_to_add = SS_totals[z]#[0]
					
			
			
			best_clustering.append(best_clustering_to_add)
		complete_ss_totals.append(SS_totals)
		curr_best = best_clustering[0][1]
		curr_best_cluster = best_clustering[0][0]
		for best in best_clustering:
			if best[1] < curr_best:
				curr_best = best[1]
				curr_best_cluster = best[0]
		three_best_clustering.append(curr_best_cluster)
	print("finished getting 3 best")
	

	for j in range(0,3):
		list_to_plot = []
		for x in range(len(complete_ss_totals[j])):
			list_to_plot.append(complete_ss_totals[j][x][1])
		#print(list_to_plot)
		plt.plot(list_to_plot)
		curr_title = 'The ss_totals for k-means clustering where k = ',(j+3)
		plt.title(curr_title)
		plt.ylabel('ss_totals')
		if j != 2:
			plt.figure()
	#plt.show()		
		 
	fig = plt.figure(4, figsize=(8, 6))
	ax = Axes3D(fig, elev=-150, azim=110)
	centroids=[]
	Y=[]
	X=[]
	data = []
	color=0
	colors=["purple","red","cyan","blue","green"]
	for cluster in three_best_clustering:
		for centroid in cluster.keys():
			centroids.append(ast.literal_eval(centroid))
			for idx in cluster[centroid]:
				X.append(idx[0:4])
				Y.append(colors[color])
			#ax.scatter([cluster[0][1]],[cluster[0][2]],cluster[0][3],c=colors[color],marker='*',s=[200])
			color+=1
		color = 0
	X=np.array(X)
	print(centroids)
	print(X)

	ax.scatter(X[:, a1], X[:, a2], X[:, a3], c=Y,
	           cmap=plt.cm.Paired)

	title=["Sepal Length","Sepal Width","Petal Length","Petal Width"]
	ax.set_title("Best Clustering:")
	ax.set_xlabel(title[1])
	ax.w_xaxis.set_ticklabels([])
	ax.set_ylabel(title[2])
	ax.w_yaxis.set_ticklabels([])
	ax.set_zlabel(title[3])
	ax.w_zaxis.set_ticklabels([])

	plt.show()		


	#graph that stuff
	#use sklearn to plot the 3d cluster in 4 different ways 






