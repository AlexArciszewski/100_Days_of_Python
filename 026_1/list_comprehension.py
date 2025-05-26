numbers = [1,2,3,4]

new_list = []
print(new_list)
new_list = [x for x in numbers]
print(new_list)
another_new_list = [x for x in numbers if x % 2 == 0]
print(another_new_list)

newer_list = [x +1 for x in numbers if x % 2 == 0]
print(newer_list)

name = "Angela"
print(name)
new_list =[letter for letter in name]
print(new_list)
print("".join(new_list))


doubled_num:list = [x*2 for x in range(1,5)]
print(doubled_num)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freedie"]

shorts = [name for name in names if len(name) < 5]
print(shorts)

capital_long_names = [name.upper() for name in names if len(name) > 5]
print(capital_long_names)

list1 = [1,2,3]
list2 = [2,3,4]
result = [number for number in list1 if number in list2]

print(result)


