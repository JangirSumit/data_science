import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder

# 1.Load the data from “college.csv” that has attributes collected about private and public colleges 
# for a particular year. We will try to predict the private/public status of the college from other attributes.
data = pd.read_csv("College.csv")
data.head()

labelencoder = LabelEncoder()
data["Private"] = labelencoder.fit_transform(data["Private"])
data.head()


# 2.Use LabelEncoder to encode the target variable in to numerical form and split the data such that 20% of the data is set aside fortesting.
X = data.iloc[:,1:]
Y = data["Private"]

train_x, test_x, train_y, test_y = train_test_split(X, Y, test_size = 0.30, random_state = 10)


# 3.Fit a linear svm from scikit learn and observe the accuracy.[Hint:Use Linear SVC
model_svm = svm.LinearSVC()
model_svm.fit(train_x, train_y)
predicted_values = model_svm.predict(test_x)

print("\nAccuracy Score\n")
print(metrics.accuracy_score(predicted_values, test_y))


# 4.Preprocess the data using StandardScalar and fit the same model again and observe the change in accuracy.
# [Hint: Refer to scikitlearn’s preprocessing methods]
# http://benalexkeen.com/feature-scaling-with-scikit-learn/
from sklearn.preprocessing import StandardScaler
scaler_df = StandardScaler().fit_transform(X)
scaler_df = pd.DataFrame(X, columns=X.columns)

X = scaler_df
Y = data["Private"]

train_x, test_x, train_y, test_y = train_test_split(X, Y, test_size = 0.30, random_state = 10)

model_svm = svm.LinearSVC()
model_svm.fit(train_x, train_y)

predicted_values = model_svm.predict(test_x)
metrics.accuracy_score(predicted_values, test_y)

# 5.Use scikit learn’s gridsearch to select the best hyperparameter for a non-linear SVM,identify the model with 
# best score and its parameters.
# [Hint: Refer to model_selection module of Scikit learn]