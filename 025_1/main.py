import pandas as pd

with open("weather_data.csv",mode="r") as data:
    values = data.readlines()
    print(values)
#['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    print(data) #<_csv.reader object at 0x00000280A4E7F2E0>
    for row in data:
        print(row)
        temperatures.append(row[1])
print(temperatures)
temperatures.remove('temp')
print(temperatures)
temperatures_int = [int(x) for x in temperatures]
print(temperatures_int)
temperatures = temperatures_int

print("opcja nr 2")
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

df = pd.read_csv("weather_data.csv")
print(df)
print(df['temp'])

df_dict = df.to_dict()
print(df_dict)




data = pd.read_csv("weather_data.csv")
df_series_to_list = data["temp"].to_list()

print(df_series_to_list)

"Lists"
avg_temp = sum(df_series_to_list)/len(df_series_to_list)
print(avg_temp)

"Pandas"
pd_avg_temp = df['temp'].mean()
print(pd_avg_temp)



pd_max_temp = df['temp'].max()
print(pd_max_temp)

print(df)

#kolumna
print(df['condition'])
print(df.condition)
#wiersz
print(df[df.day =="Monday"])
#max temp
print("Opcja 1")
print(df[df['temp'] == df['temp'].max()])
print("Opcja 2")
print(df[df.temp == df.temp.max()])

monday = df[df.day == "Monday"]
print(monday) #0  Monday    12     Sunny
print(monday.condition) #0    Sunny

print(monday.temp) #0    12
print(monday.temp[0])    #12
print((monday.temp[0]*9/5) + 32)


data_dict = {
    'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'},
    'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24},
    'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}
    }

#tworzenie nowego slownika
data = pd.DataFrame(data)
data.to_csv("new_dict.csv")
print(data_dict)