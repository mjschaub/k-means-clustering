
import numpy as np
import ast
import math


def euclidean_dist(a,b):
	dist = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2 + (a[3]-b[3])**2)	
	return dist


def change_centroids(clustering,remove_data):

	print('changing centroids')
	if remove_data is True:
		for i in clustering.keys():
			if clustering[i] == []:
				del clustering[i]
				continue
			new_centroid = [0.0,0.0,0.0,0.0]
			for j in clustering[i]:
				for z in range(len(j)):
					if z == 4:
						break
					new_centroid[z]+=j[z]
		
			new_centroid = [x/len(clustering[i]) for x in new_centroid]
			del clustering[i]
			clustering[repr(new_centroid)] = []
	else:
		for i in clustering.keys():
			if clustering[i] == []:
				del clustering[i]
				continue
			new_centroid = [0.0,0.0,0.0,0.0]
			for j in clustering[i]:
				for z in range(len(j)):
					if z == 4:
						break
					new_centroid[z]+=j[z]
		
			new_centroid = [x/len(clustering[i]) for x in new_centroid]
			clustering[repr(new_centroid)] = clustering[i]
			

def calc_SS_total(clustering):
	total_sum = 0
	for i in clustering.keys():
		for j in clustering[i]:
			total_sum+= euclidean_dist(j[0:4],ast.literal_eval(i))**2
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
	for j in(0,3):
		print 'doing a k-means run for index: ',(j+3)
		SS_totals = []
		best_clustering = []
		for i in range(0,3): # 0 for 5 times, 1 for 10, 2 for 20
			print 'beginning the four cluster attempts for range ', i
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
				print('calculating ss_totals')
				SS_totals.append((curr_clustering, calc_SS_total(curr_clustering)))
			print(SS_totals[0])
			print(len(SS_totals))
			best_ss = SS_totals[i*4][1]
			best_clustering_to_add = SS_totals[i*4][0]
			for z in range(i*4,4*(i+1)):
				if SS_totals[z][1] < best_ss:
					best_ss = SS_totals[z][1]
					best_clustering_to_add = SS_totals[z][0]
			print('best clustering: ',best_clustering_to_add)
			best_clustering.append(best_clustering_to_add)
		complete_ss_totals.append(SS_totals)
		three_best_clustering.append(best_clustering)
	print(complete_ss_totals)
	print(three_best_clustering)

				 
		
	
	#graph that stuff
	#use sklearn to plot the 3d cluster in 4 different ways 






