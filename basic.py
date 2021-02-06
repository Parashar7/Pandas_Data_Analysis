import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

data_df = pd.read_csv('covid_fulldata.txt')
# RETRIVING DATA FROM FILE

# print(data_df)
# print(data_df.describe())
# print(data_df.info())
print(data_df.columns)
# print(data_df.shape)
# print(type(data_df))
# print(data_df['new_cases'][20134])
##new_df= data_df[['new_cases', 'total_cases']]
# print(new_df)
# print(data_df.loc[234])
# print(data_df.head(20))
# print(data_df.tail(4))
# print(data_df.weekly_cases.first_valid_index())
# print(data_df.loc[108:113])
new_data = data_df[['date', 'location', 'new_cases', 'new_deaths']]
# print(new_data)
# print(new_data.loc[333])
# print(new_data.at[333, 'new_cases'])
# print(new_data.sample(10))


# ANALYSING DATA FROM FILE

totaldeath = new_data.new_deaths.sum()
totalcases = new_data.new_cases.sum()
# print('Total Death is', totaldeath, 'and total Case is', totalcases)
death_rate = totaldeath / totalcases
# print('Death rate is', death_rate*100, '%')

# QUERY AND COMPARISON

high_new = new_data.new_cases > 1000
# print(high_new[133:140])
# print(high_new.size)

# print(new_data.loc[130:140])

high_new1_df = new_data[new_data.new_cases > 1000]
# print(high_new1_df[133:140])

# SORTING ROWS USING COLUMN VALUES

sort = new_data.sort_values('new_cases', ascending=False).head(10)
# print(sort)

# CHANGING VALUE
# initial value is 113
# print(new_data.at[136, 'new_cases'])
# new_data.at[136, 'new_cases']= (new_data.at[135,'new_cases']+new_data.at[137, 'new_cases'])/2

# print(new_data.at[136, 'new_cases'])

# WORKING WITH DATES

# print(data_df.date)
# print(data_df['date'])

data_df['date'] = pd.to_datetime(data_df.date)

print(data_df['date'])

data_df['year'] = pd.DatetimeIndex(data_df.date).year
# print(data_df)

data_df['month'] = pd.DatetimeIndex(data_df.date).month
print(data_df)

data_df['weekday'] = pd.DatetimeIndex(data_df.date).weekday
# print(data_df)

data_df['day'] = pd.DatetimeIndex(data_df.date).day
# print(data_df)

# print('\t\t\t\t\t\t\t\t\t\t\tNew DataFrame\n\n', data_df)

# m= int(input('Enter a month number:'))
# month_value= data_df[data_df.month==m]
# print('Month containing month number', m,'\n\n',  month_value)

# MEAN

# mean_value= data_df[data_df.weekday==4].new_cases.mean()
# print('Mean vale is', mean_value)

# GROUPING AND AGGREGATION, gives the month wise sum, mean, median etc...
# print(data_df.columns)
# group_dataframe= data_df.groupby('month')[['new_cases', 'new_deaths', 'total_cases', 'total_deaths']].mean()
# print(group_dataframe)

# data_df['final_cases']=data_df.new_cases.cumsum()
# print(data_df)
# plot= data_df['new_cases'].plot()
# print(plot)

# PLOTTING GRAPHS

# new_data['date']= pd.to_datetime(new_data.date)
# print(new_data)
# df = DataFrame(new_data.loc[100:200], columns=['date', 'new_cases'])
# df.plot(x='date', y='new_cases', kind= 'scatter')
# plt.show()


# df = DataFrame(new_data.loc[100:200], columns=['new_deaths'])
# df.plot()
# plt.show()

# df = DataFrame(new_data.loc[100:150], columns=['new_cases', 'new_deaths'])
# df.plot()
# plt.show()


death_rate = data_df.loc[100:200].total_deaths / data_df.loc[100:200].total_cases
print(death_rate)

# date_data= data_df.set_index('date', inplace=True)
# print(date_data)

df = DataFrame(data_df, columns=['death_rate'])
death_rate.plot(x='month', y='death_rate', title='Death Rate')
plt.show()
