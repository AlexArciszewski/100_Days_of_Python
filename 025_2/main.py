import pandas as pd



df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(df)
print(df.head())
print(df.shape)
print(df.info())
# print(df.describe())
color = df['Color notes']
print(color)
unique_colors = df['Color notes'].unique()
print(unique_colors)
color_combination = df['Combination of Primary and Highlight Color'].unique()
print(color_combination)
primary_color = df['Primary Fur Color']
print(primary_color)
grey_squirrel = df[df['Primary Fur Color'] == "Gray"]
count_grey_squirrel = (df['Primary Fur Color'] == "Gray").sum()
print(count_grey_squirrel) #2473
count_red_squirrel = (df['Primary Fur Color'] == "Cinnamon").sum()
print(count_red_squirrel)   #392
count_black_squirrel = (df['Primary Fur Color'] == "Black").sum()
print(count_black_squirrel) #Black

print(df['Primary Fur Color'].unique())


final_table = {
    'Fur Color':{0:'grey', 1:'red',2:'black'},
    "Count":{0:count_grey_squirrel, 1:count_red_squirrel, 2:count_black_squirrel}
            }

table = pd.DataFrame(final_table)
table.to_csv('table.csv')



















