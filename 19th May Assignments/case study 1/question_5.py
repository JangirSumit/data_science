# 5.Perform Operations on Files
# 5.1: From the raw data below create a data frame
# 'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
# 'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
# 'age': [42, 52, 36, 24, 73],
# 'preTestScore': [4, 24, 31, ".", "."],
# 'postTestScore': ["25,000", "94,000", 57, 62, 70]
# 5.2: Save the dataframe into a csv file as example.csv
# 5.3: Read the example.csv and print the data frame
# 5.4: Read the example.csv without column heading
# 5.5: Read the example.csv andmake the index columns as 'First Name’ and 'Last Name'
# 5.6:  Print  the  data  frame  in  a  Boolean  form  as  True  or  False.
# True  for  Null/  NaN values and false for non-nullvalues
# 5.7: Read the dataframe by skipping first 3 rows and print the data frame
# 5.8: Load a csv file while interpreting "," in strings around numbers as thousands seperators.
# Check the raw data 'postTestScore' column has, as thousands separator.
# Comma should be ignored while reading the data. It is default behaviour,
# but you need to give argument to read_csv function which makes sure commas are ignored.

import pandas as pd

# 5.1
df = pd.DataFrame({'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
                   'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
                   'age': [42, 52, 36, 24, 73],
                   'preTestScore': [4, 24, 31, ".", "."],
                   'postTestScore': ["25,000", "94,000", 57, 62, 70]})


# 5.2
df.to_csv("example.csv")
print("*"*20)

# 5.3
df = pd.read_csv("example.csv")
print(df)
print("*"*20)

# 5.4
df_without_header = pd.read_csv("example.csv", header=None)
print(df_without_header)
print("*"*20)

# 5.5
df_with_index = pd.read_csv("example.csv", index_col=[
                            "first_name", "last_name"])
print(df_with_index)
print("*"*20)

# 5.6
boolean_df = df.isnull().any()
print(boolean_df)
print("*"*20)

# 5.7
df_skip_rows = pd.read_csv("example.csv", skiprows=3)
print(df_skip_rows)
print("*"*20)

# 5.8
