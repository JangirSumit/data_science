import numpy as np
import pandas as pd

df_ratings = pd.read_csv("BX-Book-Ratings.csv", encoding="latin1")
df_ratings.head()

df_books = pd.read_csv("BX-Books.csv", encoding="latin1", low_memory=False)
df_books.head()

df_users = pd.read_csv("BX-Users.csv", encoding="latin1", low_memory=False)
df_users.head()