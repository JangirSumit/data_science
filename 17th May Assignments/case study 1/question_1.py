# 1.Find the highest rated movie in the“Quest” story type.

import pandas as pd

df = pd.read_csv('HollywoodMovies.csv')

highest_rate = df[df["Story"] == "Quest"]["RottenTomatoes"].max()

highest_rated_movies = df[df["RottenTomatoes"] == highest_rate]

print(highest_rated_movies)
