import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

data_df = pd.read_csv('covid_fulldata.txt')

# print(data_df)

# print(data_df.describe())

# print(data_df.columns)

# print(data_df.info())

# print(data_df.shape)

# print(type(data_df['new_cases']))

death_rate = data_df.total_deaths / data_df.total_cases
print('Death rate is\n\n', death_rate)

data_df['date'] = pd.to_datetime(data_df.date)

# print(data_df.info())

data_df['month'] = pd.DatetimeIndex(data_df.date).month
df_grouped = (data_df.groupby(['month']))
df_grouped.plot.bar(x='month', y='death_rate', color='blue')

data_df['Death Rate'] = death_rate
result_df = data_df[[
    'date',
    'month',
    'new_cases',
    'new_deaths',
    'Death Rate'
]]
#group_dataframe = data_df.groupby('month')
result_df.to_csv('result.csv', index=None)
print(result_df)
# print(result_df.to_csv('results.csv', index=None))
# print(result_df)
# print(data_df.info())
# print(data_df)
df = DataFrame(result_df.loc[100:150], columns=['month', 'Death Rate'])
df.plot(x='month', y='Death Rate', title='Death Rate', kind='bar')
plt.show()



#df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
#df.groupby([df['Date'].dt.month_name()], sort=False).mean().eval('A+B')\
#  .plot(kind='bar')

#df_grouped = (df.groupby(['month'])
 #               .size()
 #               .reset_index(name="n_pets"))
