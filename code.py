import csv
import pandas as pd
import plotly.express as plotly

df = pd.read_csv("data.csv")

f = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
fig = plotly.scatter(f, x="student_id", y="level", size="attempt", color="attempt")
fig.show()