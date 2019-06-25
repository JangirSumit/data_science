from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split, cross_val_score, KFold, ShuffleSplit, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv("glass.csv")
data.head()


print("Unique Types")
print(data['Type'].unique())

sns.countplot(data["Type"])
plt.show()


X = data.iloc[:, 0:9]
print(X.head())


Y = data["Type"]
print(Y.head())


train_x, test_x, train_y, test_y = train_test_split(
    X, Y, random_state=5, test_size=0.30)


dt_model = DecisionTreeClassifier()
dt_model.fit(train_x, train_y)


predicted = dt_model.predict(test_x)

print("Root Mean Square Error")
rms = metrics.mean_squared_error(predicted, test_y)
print(rms)

print("Accuracy Square")
print(metrics.accuracy_score(predicted, test_y))


kf = KFold(n_splits=3)

for train_index, test_index in kf.split(X):
    #rint("TRAIN:", train_x, "TEST:", test_x)
    x_train, x_test = X.loc[train_index], X.loc[test_index]
    y_train, y_test = Y[train_index], Y[test_index]

    dt_model.fit(x_train, y_train)
    predicted = dt_model.predict(x_test)
    print("Accuracy Score : " +
          str(metrics.accuracy_score(predicted[0:], y_test.values)))


print(cross_val_score(dt_model, X, Y, cv=3, scoring="accuracy").mean())


rf_model = RandomForestClassifier(
    n_jobs=-1, max_features='sqrt', n_estimators=50, oob_score=True)
parameter_candidates = [{1}, {2}]
param_grid = {
    'n_estimators': [100, 200],
    'max_features': ['auto', 'sqrt', 'log2']
}

CV_rfc = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5)
CV_rfc.fit(X, Y)
print(CV_rfc.best_params_)


rf_model = RandomForestClassifier(
    n_jobs=-1, max_features='auto', n_estimators=200, oob_score=True)
print(cross_val_score(rf_model, X, Y, cv=10, scoring='accuracy'))
