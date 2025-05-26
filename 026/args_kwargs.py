student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}





#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


import pandas as pd
letters_nato_dict = {}
read_data = pd.read_csv("nato_phonetic_alphabet.csv")
print(read_data)

print("opcja nr 1")
for index, row in read_data.iterrows():
    print(index, row['letter'], row['code'])

letters = []
code = []

for index, row in read_data.iterrows():
    letters.append(row['letter'])
    code.append(row['code'])
print(letters)
print(code)


letters_nato_dict = dict(zip(letters,code))


final_list =[]
word = input("pls give me the word: ")
# for letter in word:
#     if letter in letters_nato_dict.keys():
#         final_list.append(letters_nato_dict[letter])
# print(final_list)
final_list = [letters_nato_dict[letter] for letter in word if letter in letters_nato_dict.keys()]
print(final_list)