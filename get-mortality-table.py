import pandas as pd 

url = "https://www.ssa.gov/oact/STATS/table4c6.html"
df = pd.read_html(url,index_col=None)[0]


# for col in df.columns:
#     print(col)

# df.columns = df.columns.get_level_values(1)

df.columns = ["age","male_qx","male_lx","male_le","female_qx","female_lx","female_le"]

# clean up
df.drop(df.tail(2).index,inplace=True)
print(df.head())
print(df.shape)
df.to_csv("mortality.csv",index=None)