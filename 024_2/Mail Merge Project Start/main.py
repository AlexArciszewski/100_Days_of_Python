#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open(r"C:\Users\arcis\PycharmProjects\100_days_of_code\024_2\Mail Merge Project Start\Input\Letters\starting_letter.txt", mode="r") as starting_letter:
    #print(starting_letter.readlines())
    starting_letter:str = starting_letter.read()

letter_list = starting_letter.split()
print(letter_list)



with open(r"C:\Users\arcis\PycharmProjects\100_days_of_code\024_2\Mail Merge Project Start\Input\Names\invited_names.txt", mode="r") as names:
    #print(names.readlines())
    names_inside:str = names.read()
    print(names_inside)

names_list:list[str] = names_inside.split()
print(names_list)

index:int = letter_list.index('[name],')
print(index)

word:str = letter_list[index]
print(word)
word:str = word.replace(",","")
print(word)
letter_list[index]:str = word
print(letter_list)

letter_list.insert(index+ 1,",")
print(letter_list)

i:int = len(names_list)
print(i)

list_of_lists:list = []

for name in names_list:
    letter_list_copied:list = letter_list.copy()
    for i, word in enumerate(letter_list_copied):
        if word == "[name]":
            letter_list_copied[i]:str = name

    list_of_lists.append(letter_list_copied)
    letter_text_copied = " ".join(letter_list_copied)
    with open(f"./Output/ReadyToSend/letter_for_{name}.docx",mode="w", encoding="utf-8") as file:
        file.write(letter_text_copied)



















