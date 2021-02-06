import pandas as pd

data_df = pd.read_csv('covid_fulldata.txt')

print(data_df)

data_df.new_cases.plot()
pd.show()

