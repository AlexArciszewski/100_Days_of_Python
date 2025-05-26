# dict ={}
# new_dict = {new_key:new_value for (key, value) in dict.items()}

import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freedie"]


scores = []

for name in names:
    score = random.randint(1,100)
    scores.append(score)
print(scores)

paired = dict(zip(names, scores))
print(paired)

print("opcja B")
dict_comprehension = {name:random.randint(1,100) for name in names}
print(dict_comprehension)

passed_students = {name: score for (name, score) in dict_comprehension.items() if score > 60}
print(passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list_of_words = sentence.split(" ")
print(list_of_words)
counter = [len(word) for word in list_of_words]
print(counter)
dict_word_num = dict(zip(list_of_words,counter))
print(dict_word_num)

print('2')

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
other_dict_word_num = {word:len(word) for word in sentence.split(" ")}
print(other_dict_word_num)


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:((temp*9/5) + 32) for (day,temp) in weather_c.items()}
print(weather_f)
# dict ={}
# new_dict = {new_key:new_value for (key, value) in dict.items()}

import pandas

student_dict = {
    "student": ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freedie"],
    "score": [70,80,79,34,24,23]
    }

for key, value in student_dict.items():
    print(value, key)

# z pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
#
#     student  score
# 0      Alex     70
# 1      Beth     80
# 2  Caroline     79
# 3      Dave     34
# 4   Eleanor     24
# 5   Freedie     23


for key, value in student_data_frame.items():
    print(key)
# student
# score


for key, value in student_data_frame.items():
    print(value)

# 0    70
# 1    80
# 2    79
# 3    34
# 4    24
# 5    23
# Name: score, dtype: int64

for index, row in student_data_frame.iterrows():
    print(row)
#rząd to obiekt Series

for index, row in student_data_frame.iterrows():
    if row.student == "Freedie":
        print(row.score)
#23











