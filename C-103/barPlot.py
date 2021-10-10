import pandas as pd
from pandas.core.reshape import tile
import plotly_express as px

df=pd.read_csv("data.csv")
fig=px.bar(df,x="Country",y="InternetUsers")
fig.show()