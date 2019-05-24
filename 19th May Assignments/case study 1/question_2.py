# 2. Find the genre in which there has been the greatest number of movie releases

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('HollywoodMovies.csv')

genre_groups = df.groupby("Genre").groups

genre_groups.keys()

plt.bar(genre_groups.keys(), [len(values) for values in genre_groups.values()])
plt.xlabel("Genre")
plt.ylabel("Number of movies")
plt.title("Genre vs Number of Movies")

plt.setp(plt.gca().get_xticklabels(), rotation=90, horizontalalignment='right') # Rotate Axis Labels

plt.grid()
plt.show()

# By seeing plot we can clearly see that Genre which is having most number of movies is -
# Comedy
