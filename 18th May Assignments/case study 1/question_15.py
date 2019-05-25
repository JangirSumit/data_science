# 15.Analyse  various  school  outcomes  in  Tennessee  using  pandas.
# Suppose  you  are  a public   schooladministrator.   Some   schools   in   your
# state   of   Tennessee   are performing  below  average  academically.  Your  superintendent,
# under  pressure from frustrated parents and voters, approached you with the task of understanding
# why  these  schools  are  under-performing.To  improve  school  performance,  you need to
# learn more about these schools and their students, just as a business needs to understand
# its own strengths and weaknesses and its customers. Though you is eager  to  build  an
# impressive  explanatory  model,  you  knowthe  importance  of conducting  preliminary
# research  to  prevent  possible  pitfalls  orblind  spots.  Thus, you engages in a
# thorough exploratory analysis, which includes: a lit review, data collection, descriptive
# and inferential statistics, and data visualization.

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns

# Phase 1 -Data CollectionHere  is  a  data  of  every  public  school  in  middle  Tennessee.
# The  data  also  includes various  demographic,  school  faculty,  and  income  variables.
# You  need  to  convert  the data into useful information.
# •Read the data in pandas data frame
# •Describe the data to find more details
df_school_data = pd.read_csv("middle_tn_schools.csv")
print(df_school_data.head())
df_school_data.describe()

# Phase 2 -Group data by school ratingsChooses  indicators  that  describe  the  student
# body  (for  example,reduced_lunch)  or school administration (stu_teach_ratio) hoping
# they will explainschool_rating.reduced_lunchis  a  variable  measuring  the  average
# percentage of students per school enrolled in a federal program that provides lunches
# for students from lower-income households. In short,reduced_lunchis a good proxy for
# household income. Isolates‘reduced_lunch’and groups the data by‘school_rating’using
# pandasgroupby method and then usesdescribeon the re-shaped data
df_grouped_data = df_school_data.groupby("school_rating").describe()
print(df_grouped_data.head())

# Phase 3 –Correlation analysisFind the correlation between ‘reduced_lunch’and‘school_rating’.
# The values in the correlation matrix table will be between -1 and 1. A value of -1 indicates
# the strongest possible negative correlation, meaning as one variable decreases the other increases.
# And a value of 1 indicates the opposite.
corrmat = df_grouped_data.corr()
print(corrmat)
f, ax = plt.subplots(figsize=(9, 8))
sns.heatmap(corrmat, ax=ax, cmap="YlGnBu", linewidths=0.1)

# Phase 4 –Scatter PlotFind the relationship betweenschool_ratingandreduced_lunch, Plot a graph
# with the two variables on a scatter plot. Each dot represents a school. The placement of the
# dot represents that school's rating (Y-axis) and the percentageof its students on reduced
# lunch    (x-axis).    The    downward    trend    line    shows    the    negative
# correlation betweenschool_ratingandreduced_lunch(as one increases, the other decreases).
# The slope of the trend line indicates how muchschool_ratingdecreases asreduced_lunchincreases.
# A  steeper  slope  would  indicate  that  a  small  change inreduced_lunchhas  a  big  impact
# onschool_ratingwhile  a  more  horizontal  slope would  indicate  that  the  same  small  change
# inreduced_lunchhas  a  smaller  impact onschool_rating
plt.scatter(df_school_data["school_rating"], df_school_data["reduced_lunch"])
plt.grid()
plt.xlabel("Rating")
plt.ylabel("Reduced lunch")
plt.title("School rating vs Reduced lunch")
plt.show()
