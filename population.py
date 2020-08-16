import pandas as pd
import calendar

# =========  Quarterly population ==========
df1= pd.read_csv("/Users/afrida/Documents/Course/covid-govhack/data_to_use/update1.csv")

df2= pd.read_csv("/Users/afrida/Documents/Course/covid-govhack/data_to_use/quarterlypop.csv")
df2['population']= df2['population']*0.0118 + df2['population']

df2 = df2.drop(['month'], axis=1)
print(df1.head(10))
print(df2.head(10))
df1['month'] = df1['month'].str[:3]
print(df1.head(5))
df1.to_csv(r'/Users/afrida/Documents/Course/covid-govhack/data_to_use/final/covidunemploy.csv', index = False, header=True)


df2['month'] = df2['month'].apply(lambda x: calendar.month_abbr[x])
print(df2.head(10))
# df3 = pd.concat([df1,df2])
df3 =pd.merge(df1, df2, on=["state_abbrev"])
# df3 =pd.merge(df1, df2, how='left', left_on=['state_abbrev'], right_on = ['state_abbrev'])
df3['population']= df3['population']*0.0118 + df3['population']

print(df3.head(10))

df2.to_csv(r'/Users/afrida/Documents/Course/covid-govhack/data_to_use/final/covidpop.csv', index = False, header=True)
df3.to_csv(r'/Users/afrida/Documents/Course/covid-govhack/data_to_use/final/covidpop2.csv', index = False, header=True)
# print(df3.head(10))


df= pd.read_csv("/Users/afrida/Documents/Course/covid-govhack/data_to_use/addedpop.csv")
df['month']= df['month']+str("-20")
df = df.dropna(axis=0)
# print(df)
df.to_csv(r'/Users/afrida/Documents/Course/covid-govhack/data_to_use/final/popunemploycovid.csv', index = False, header=True)


# ======= final =====
finaldata = pd.read_csv("/Users/afrida/Documents/Course/covid-govhack/data_to_use/final/updateFinal.csv")
# print(finaldata.columns)

# ========= MLP on final ====
from sklearn.model_selection import train_test_split
import keras
from keras.models import Sequential
from keras.layers import Activation, Dense


finaldata = pd.read_csv("/Users/afrida/Documents/Course/covid-govhack/data_to_use/experiment_mlp.csv")
# print(finaldata.columns)
# y = Number of vaccines
y = finaldata.pop('Number of vaccines')
X = finaldata
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2)
# print(y_train)
# define model
model = Sequential()
n_steps =12
model.add(Dense(100, activation='relu', input_dim=n_steps))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')
# fit model
# model.fit(X, y, epochs=2000, verbose=0)
