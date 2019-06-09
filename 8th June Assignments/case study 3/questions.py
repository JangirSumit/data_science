from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("zoo.csv")
data.head()


unique_classtypes = np.unique(data["class_type"].values)

agglo = AgglomerativeClustering(n_clusters=16)
agglo.fit(data.iloc[:, 1:])
