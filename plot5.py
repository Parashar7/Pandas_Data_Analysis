import pandas as pd

filename = "aac_shelter_cat_outcome_eng.csv"
df = pd.read_csv('result1.txt',
                 usecols=['month', 'Death Rate']
                 )
df.head()
df['date'] = pd.to_datetime(df.date)

df['month'] = pd.DatetimeIndex(df.date).month
# df['Death Rate'] = pd.DatetimeIndex(df['date_of_birth']).weekday_name
df_grouped = (df.groupby(['month'])
              .size()
              .reset_index(name="n_pets"))
df_grouped

df_grouped.plot.bar(x="month", y="Death Rate", color='blue')
