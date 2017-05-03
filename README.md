# k-means-clustering
A k-means clustering and analysis done on observations in the iris dataset: https://archive.ics.uci.edu/ml/datasets/Iris 


This program runs k-means for each k=3,4,5. For each k there are 4 runs of each stopping condition of 5, 10, and 20 iterations. 
We look at the squared sums total of all 12 runs for each k and find the most efficient. Then, check the F1 scores of the 3 clusterings
for each k and create a 3d plot in 4 different ways (since the data is in 4d) to visualize the best clustering. Different clusters are colored
differently with the centroids being represented as stars. 
