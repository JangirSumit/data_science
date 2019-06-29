import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data collection and reading
# decimal : set character used for decimal numbers
data = pd.read_csv("Project_Data_1.csv", index_col=0, decimal=",")
data.head()

# check null, nan values
data.isna()

# drop nan values if exists
data.dropna()


# data splitting for clustering
data_for_decomposition = data.iloc[:, 0:]
data_for_decomposition.head()


# PCA for dimension reduction
model_pca = PCA(n_components=2)
pca_data = model_pca.fit(data_for_decomposition).transform(
    data_for_decomposition)

new_data = pd.DataFrame(pca_data, columns=["pca_1", "pca_2"])
new_data.index = data.index
new_data.head()


# elbow method to find number of clusers
wcss = []  # wcss - within cluster squared sum of inertia

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++',
                    max_iter=300, n_init=10, random_state=10)
    kmeans.fit(new_data)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("wcss")
plt.show()
# It indicates the number of clusters will be 3

# Kmeans Algorithm
kmeans = KMeans(n_clusters=3)
# fir the model
kmeans.fit(new_data)
# clusters centers
print(kmeans.cluster_centers_)

# adding cluster column
new_data["cluster"] = kmeans.labels_
new_data.head()

# plotting the cluster data
sns.lmplot('pca_1', 'pca_2', data=new_data, hue='cluster',
           palette='coolwarm', height=6, aspect=1, fit_reg=False)


# adding cluster column to original data
data["cluster"] = kmeans.labels_


# export data for analysing
new_data.sort_values(["cluster", "pca_1", "pca_2"])
new_data.to_csv("output.csv", index=True)


# Largest Importer and constantly increasing
data.loc["Sierra Leone"]
X = data.loc["Sierra Leone"].index[0:18]
Y = data.loc["Sierra Leone"].values[0:18]

plt.bar(X, Y)
plt.setp(plt.gca().get_xticklabels(), rotation=90,
         horizontalalignment='right')  # Rotate Axis Labels

plt.show()


# most consistent
data.loc["Monaco"]
X = data.loc["Monaco"].index[0:18]
Y = data.loc["Monaco"].values[0:18]

plt.bar(X, Y)
plt.setp(plt.gca().get_xticklabels(), rotation=90,
         horizontalalignment='right')  # Rotate Axis Labels

plt.show()
