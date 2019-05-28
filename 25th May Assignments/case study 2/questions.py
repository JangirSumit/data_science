from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the data from “cereal.csv” and plot histograms of sugar and vitamin content across different cereals
df_cereal = pd.read_csv("cereal.csv")
print(df_cereal.head())

plt.hist([df_cereal["sugars"], df_cereal["vitamins"]],
         color=['orange', 'green'])
plt.title("Sugars and Vitamins")
plt.xlabel("Sugars and Vitamins")
plt.legend(["Sugars", " Vitamins"])
plt.show()


# 2. The names of the manufactures are coded using alphabets, create a new column with their fullname using the below mapping.
# 'N': 'Nabisco',
# 'Q': 'Quaker Oats',
# 'K': 'Kelloggs',
# 'R': 'Raslston Purina',
# 'G': 'General Mills' ,
# 'P' :'Post' ,
# 'A':'American Home Foods Products'
# Create a bar plot where each manufacturer is on the y axis and the
# height of the bars depict the number of cereals manufactured by them.

dict_mfr = {'N': 'Nabisco',
            'Q': 'Quaker Oats',
            'K': 'Kelloggs',
            'R': 'Raslston Purina',
            'G': 'General Mills',
            'P': 'Post',
            'A': 'American Home Foods Products'}

df_cereal["manufactures"] = [dict_mfr[mfr] for mfr in df_cereal["mfr"]]

grouped_mfr = df_cereal.groupby(["manufactures"], as_index=False).count()
x = grouped_mfr["manufactures"]
y = grouped_mfr["mfr"]

plt.bar(x, y)

plt.setp(plt.gca().get_xticklabels(), rotation=90, horizontalalignment='right')
plt.xlabel("Manufactureres")
plt.ylabel("Count")
plt.title("number of cereals manufactured by Manufactures")
plt.show()


# 3. Extract the rating as your target variable ‘y’ and all numerical parameters as your predictors ‘x’.
# Separate 25% of your data as test set.


X = df_cereal.iloc[:, 3:15]
Y = df_cereal["rating"]

x_train, x_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.25, random_state=10)


# 4. Fit a linear regression module and measure the mean squared error on test dataset.
# [ Hint: Explore linear models and metrics section of sklearn documentation]

liner_model = LinearRegression()
liner_model.fit(x_train, y_train)

predicted_ratings = liner_model.predict(x_test)

plt.scatter(np.array(predicted_ratings), np.array(y_test))
plt.show()
