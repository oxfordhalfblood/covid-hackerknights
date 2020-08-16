import pandas as pd
import calendar

# ================= Covid Cases ===========
df = pd.read_csv("/Users/afrida/Documents/Course/covid-govhack/data_to_use/covidcases.csv")
# print(df.head(10))
# df = covidcases['date'].dtype
df['date'] = pd.to_datetime(df['date']).dt.month
df = df.rename(columns={'date': 'month'})
df['month'] = df['month'].apply(lambda x: calendar.month_abbr[x])
df = df.sort_values(['state_abbrev'])
sum_df = df.groupby(['month', 'state_abbrev'], as_index=False)["confirmed", "deaths", "tests", "positives", "hosp", "icu", "vent" ].apply(lambda x : x.astype(int).sum()).reset_index()
# sum_df = df.groupby(['month','state_abbrev']).agg({'confirmed':'sum', 'deaths': 'sum', 'tests': 'sum', 'positives':'sum', 'hosp':'sum','icu':'sum','vent':'sum'})
# df = pd.read_csv("/Users/afrida/Documents/Course/covid-govhack/data_to_use/final/groupedstate.csv")
sum_df = sum_df.sort_values(['state_abbrev'])
sum_df['state_abbrev'] = sum_df['state_abbrev'].apply(lambda x: ' '.join(sorted(x.split())))
sum_df.to_csv(r'/Users/afrida/Documents/Course/covid-govhack/data_to_use/final/test.csv', index = False, header=True)
print(sum_df)

# ============= Employment ================

# df.to_csv(r'/Users/afrida/Documents/Course/covid-govhack/data_to_use/final/groupedstate.csv', index = False, header=True)
df2= pd.read_csv("/Users/afrida/Documents/Course/covid-govhack/data_to_use/employed_unemployed.csv")
df2 = df2.sort_values(['state-abbrev']).rename(columns={'state-abbrev': 'state_abbrev'})
df2['Month'] = df2['Month'].str[:3]
# print(df2)
df2 = df2[['Month', 'state_abbrev','Employed total', 'Unemployed total']].rename(columns={'Month': 'month'})
print(df2.head(10))
df2.to_csv(r'/Users/afrida/Documents/Course/covid-govhack/data_to_use/final/test2.csv', index = False, header=True)
# df3 = pd.concat([sum_df, df2], axis=1)
df3 =pd.merge(sum_df, df2, on=["month", "state_abbrev"])
# df3.to_csv(r'/Users/afrida/Documents/Course/covid-govhack/data_to_use/final/stateemploy.csv', index = False, header=True)
df3.to_csv(r'/Users/afrida/Documents/Course/covid-govhack/data_to_use/final/stateemploy2.csv', index = False, header=True)

df2= pd.read_csv("/Users/afrida/Documents/Course/covid-govhack/data_to_use/quarterlypop.csv")
df2['population']= df2['population']*0.0118 + df2['population']
df2['month'] = df2['month'].apply(lambda x: calendar.month_abbr[x])
print(df2.head(10))
df3 =pd.merge(df3, df2, on=["state_abbrev"])
df3.to_csv(r'/Users/afrida/Documents/Course/covid-govhack/data_to_use/final/covidpop3.csv', index = False, header=True)


# df3.to_csv(r'/Users/afrida/Documents/Course/covid-govhack/data_to_use/final/stateemploy.csv')


recoveries_by_state = pd.read_csv("/Users/afrida/Documents/Course/finance-project/recovered_2.csv")
flu_data = pd.read_csv("/Users/afrida/Documents/Course/finance-project/fluvaccine.csv")


# newformat = datetimeobject.strftime('%m-%d-%Y')

# convert into month