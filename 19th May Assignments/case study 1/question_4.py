# 4. Is there any correspondence between the critics’ evaluation of a movie and itsacceptance
# by the public? Find out, by plotting the net profitability of a movie against the
# ratings it receives on Rotten Tomatoes.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('HollywoodMovies.csv')


plt.scatter(df["RottenTomatoes"], df["AudienceScore"])
plt.show()

# Is there any correspondence between the critics’ evaluation of a movie and itsacceptance by the public?
# Yes there is a relation between them... Critics evaluation and public reponse is direcly propotional
# to each other.


# Graph between RottenTomatoes vs Profitability
plt.scatter(df["RottenTomatoes"], df["Profitability"])
plt.show()
