import pandas as pd
import matplotlib.pyplot as plt

# 1. Read the three csv files which contains the score of same students in term1 for each Subject
df_math_scores = pd.read_csv("MathScoreTerm1.csv")
df_ds_score = pd.read_csv("DSScoreTerm1.csv")
df_physics_score = pd.read_csv("PhysicsScoreTerm1.csv")

print(df_math_scores.head())
print(df_ds_score.head())
print(df_physics_score.head())


# 2. Remove the name and ethnicity column (to ensure confidentiality)
del df_math_scores["Name"]
del df_math_scores["Ethinicity"]

del df_ds_score["Name"]
del df_ds_score["Ethinicity"]

del df_physics_score["Name"]
del df_physics_score["Ethinicity"]

print(df_math_scores.head())
print(df_ds_score.head())
print(df_physics_score.head())


# 3. Fill missing score data with zero
df_math_scores.fillna(0)
df_ds_score.fillna(0)
df_physics_score.fillna(0)

print(df_math_scores.head())
print(df_ds_score.head())
print(df_physics_score.head())


# 4. Merge the three files
merged_df = df_math_scores.merge(df_ds_score, on="ID", suffixes=(
    '_math', '_ds')).merge(df_physics_score, on="ID", suffixes=('_ds', '_physics'))
merged_df_filter_cols = merged_df.filter(["ID", "Score_math", "Score_ds", "Score", "Age_math"]).rename(
    columns={"Score": "Score_physics", "Age_math": "Age"})

print(merged_df_filter_cols)


# 5. Change Sex(M/F) Columnto 1/2 for further analysis

merged_df_filter_cols["Sex"] = [1 if sex ==
                                "M" else 2 for sex in merged_df_filter_cols["Sex"]]
print(merged_df_filter_cols)


# 6. Change Sex(M/F) Columnto 1/2 for further analysis
merged_df_filter_cols.to_csv("ScoreFinal.csv")
