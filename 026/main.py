import pandas as pd

letters_nato_dict = {}
read_data = pd.read_csv("nato_phonetic_alphabet.csv")
print(read_data)

phonetic_dict = {row.letter:row.code for (index, row) in read_data.iterrows()}
print(phonetic_dict)

final_list =[]
word = input("pls give me the word: ")

final_list = [phonetic_dict[letter] for letter in word if letter in phonetic_dict.keys()]
print(final_list)

#############################################################################################################################################################


letters_nato_dict = {}
read_data = pd.read_csv("nato_phonetic_alphabet.csv")
#print(read_data)


# for index, row in read_data.iterrows():
#     print(index, row['letter'], row['code'])

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