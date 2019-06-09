import seaborn as sns
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

data = pd.read_csv("driver-data.csv", index_col="id")
data.head()

kmeans = KMeans(n_clusters=4)

kmeans.fit(data)

print("Cluster's Center\n")
print(kmeans.cluster_centers_)


# Find count of each cluster
unique, counts = np.unique(kmeans.labels_, return_counts=True)
dict_data = dict(zip(unique, counts))
print("Count of each cluster")
print(dict_data)


# Plot the clusters
data["cluster"] = kmeans.labels_
sns.lmplot('mean_dist_day', 'mean_over_speed_perc', data=data,
           hue='cluster', palette='coolwarm', size=6, aspect=1, fit_reg=False)


# Inertia is the sum of squared error for each cluster.
# Therefore the smaller the inertia the denser the cluster(closer together all the points are)
print("Inertia\n")
print(kmeans.inertia_)


# Print the data
print("Data with clusters\n")
print(data)
