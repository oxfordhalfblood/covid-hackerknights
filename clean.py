import pandas as pd
df = pd.read_csv("/Users/afrida/Documents/Course/covid-govhack/data_to_use/final/covidcases.csv")
# print(df.head(10))
# df = covidcases['date'].dtype
df['date'] = pd.to_datetime(df['date']).dt.month
df = df.rename(columns={'date': 'month'})
df = df.sort_values(['state_abbrev'])
df.to_csv (r'/Users/afrida/Documents/Course/covid-govhack/data_to_use/final/groupedstate.csv', index = False, header=True)


# recoveries_by_state = pd.read_csv("/Users/afrida/Documents/Course/finance-project/recovered_2.csv")
# big_data = pd.read_csv("/Users/afrida/Documents/Course/finance-project/6202012.xlsx")


# cereal_df2 = pd.read_csv("data/cereal.csv")
# print(cases_by_state.head(3))
# print(recoveries_by_state)
print(df.head(10))
# transposed = recoveries_by_state.T
# print(transposed)
# df = transposed[transposed.columns[1]]
# print(df.head)

# print(pd.DataFrame.equals(cereal_df, cereal_df2))

# newformat = datetimeobject.strftime('%m-%d-%Y')

# convert into month