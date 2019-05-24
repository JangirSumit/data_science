# 4. Let the x axis data points and y axis data points are
# X = [1,2,3,4]
# Y = [20, 21, 20.5, 20.8]

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

X = [1, 2, 3, 4]
Y = [20, 21, 20.5, 20.8]

# 1. Draw a Simple plot
plt.plot(X, Y)
plt.show()

#################################################################

# 2. Configure the line and markers in simple plot
plt.plot(X, Y)
plt.grid()
plt.show()

#################################################################

# 3. configure the axes
plt.setp(plt.gca().get_xticklabels(), rotation=90,
         horizontalalignment='right')  # Rotate Axis Labels

#################################################################

# 4. Give title of Graph & labels of x axis and y axis
plt.plot(X, Y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#################################################################

# 5. Give error bar if  y_error = [0.12, 0.13, 0.2, 0.1]
y_error = [0.12, 0.13, 0.2, 0.1]

plt.plot(X, Y, y_error)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#################################################################

# 6. define width, height as figsize=(4,5) DPI and adjust plot dpi=100
plt.figure(figsize=(3, 4))

#################################################################

# 7. Give a font size of 14
plt.rcParams.update({'font.size': 14})

#################################################################

# 8. Draw a scatter graph of any 50 random values of x and y axis
x = np.random.random(50)
y = np.random.random(50)

plt.scatter(x, y)
plt.show()

#################################################################

# 9. Create a dataframe from following data
# 'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
# 'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
# 'female': [0, 1, 1, 0, 1],
# 'age': [42, 52, 36, 24, 73],
# 'preTestScore': [4, 24, 31, 2, 3],
# 'postTestScore': [25, 94, 57, 62, 70]
# Draw a Scatterplot of preTestScore and postTestScore, with the size of each point determined by age
df = pd.DataFrame({
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
    'female': [0, 1, 1, 0, 1],
    'age': [42, 52, 36, 24, 73],
    'preTestScore': [4, 24, 31, 2, 3],
    'postTestScore': [25, 94, 57, 62, 70]
})

plt.scatter(df["preTestScore"], df["postTestScore"])
plt.xlabel("preTestScore")
plt.ylabel("postTestScore")
plt.title("preTestScore vs postTestScore")
plt.legend(["preTestScore", "postTestScore"])
plt.show()

#################################################################

# 10. Draw a Scatterplot from the data in question 9 of preTestScore and postTestScore
# with the size = 300 and the color determined by sex

df = pd.DataFrame({
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
    'female': [0, 1, 1, 0, 1],
    'age': [42, 52, 36, 24, 73],
    'preTestScore': [4, 24, 31, 2, 3],
    'postTestScore': [25, 94, 57, 62, 70]
})

x = df["preTestScore"]
y = df["postTestScore"]
colors = df["female"]

plt.scatter(x, y, c=colors, alpha=0.5)
plt.xlabel("preTestScore")
plt.ylabel("postTestScore")
plt.title("preTestScore vs postTestScore")
plt.legend(["preTestScore", "postTestScore"])
plt.show()
