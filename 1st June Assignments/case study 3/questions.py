import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


# Data Collection
data = pd.read_csv("breast-cancer-data.csv", index_col=0)
data.head()


# Data Wrangling
df_cancer = data
df_cancer.drop(["diagnosis"], inplace=True, axis=1)
df_cancer.head()


# Data Transformation
model_pca = PCA(n_components = 2)
model_pca.fit(df_cancer)
transformer_data = model_pca.transform(df_cancer)


# New DataFrame
new_df = pd.DataFrame(transformer_data)
new_df.index = df_cancer.index # Setting original Index
new_df.columns = ["PC1", "PC2"] # Changing Column names
new_df["diagnosis"] = data["diagnosis"] # Adding Result column
new_df.head()


#Variance Ratio
print(model_pca.explained_variance_ratio_)