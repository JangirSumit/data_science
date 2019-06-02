# https://medium.com/@parthvadhadiya424/digit-recognition-using-sk-learn-ea729fec6e3d
# http://www.thejavageek.com/2018/04/30/principal-component-analysis-using-python/

from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# 1.Scikit learn comes with pre-loaded dataset, load the digits dataset from that collection
# and write a helper function to plot the image using matplotlib.
# [Hint:Explore datasets module from scikit learn]
digits = load_digits()
plt.gray()
plt.matshow(digits.images[0])
plt.show()

images = digits.images.reshape(digits.images.shape[0], -1)
labels = digits.target


# 2.Make a train -test split with 20% of the data set aside for testing.
# Fit a logistic regression model and observe the accuracy.
train_x, test_x, train_y, test_y = train_test_split(
    images, labels, random_state=10, test_size=0.20)

log_model = LogisticRegression()
log_model.fit(train_x, train_y)

predicted_values = log_model.predict(test_x)

print("Accuracy Score\n")
print(metrics.accuracy_score(test_y, predicted_values))
print("\n\n")

# 3.Using scikit learn perform a PCA transformation such that the transformed dataset
# can explain 95% of the variance in the original dataset. Find out the number of
# components in the projected subspace.
# [Hint:Refer to decomposition module of scikit learn]

# To get 95% of variance n_components should be 10
model_pca = PCA(n_components=10)

model_pca.fit(images)

# transform the data
model_pca.fit(train_x, train_y)
train_x = model_pca.transform(train_x)
test_x = model_pca.transform(test_x)

print("Variance Ratio\n")
print(model_pca.explained_variance_ratio_)
print("\n\n")


# 4.Transform the dataset and fit a logistic regression and observe the accuracy.
# Compare it with the previous model andcomment on the accuracy.
# [Hint: Project both the train and test samples to the new subspace]'
log_model_1 = LogisticRegression()
log_model_1.fit(train_x, train_y)

predicted_values_1 = log_model_1.predict(test_x)

print("Variance Ratio\n")
metrics.accuracy_score(predicted_values_1, test_y)
print("\n\n")


# 5.Compute the confusion matrix and count the number of instances that has gone wrong.
# For each of the wrong sample,plot the digit along with predicted and original label.
conf_metrics = metrics.confusion_matrix(predicted_values_1, test_y)
classification_report = metrics.classification_report(
    predicted_values_1, test_y)

print("Confusion Metrics\n")
print(conf_metrics)
print("\n\n")

print("Classfication Report\n")
print(classification_report)
print("\n\n")
