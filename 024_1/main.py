
with open("some_text.txt","r") as file:

    from_file = file.readlines()

print(from_file)
#['Ala ma kota jest 19 maja 2025']

with open("some_text.txt","r") as file:
    print(file.read())
#Ala ma kota jest 19 maja 2025


file = open("some_text.txt")
content = file.read()
print(content)
#Ala ma kota jest 19 maja 2025
file.close()

with open("some_text.txt", mode="w", encoding="utf-8") as file2:
    file2.write("Ten tekst zastępuje Ala ma kota jest 19 maja")
#Ten tekst zastępuje Ala ma kota jest 19 maja nadpisuje to co jest wczesniej czyli Ala ma kota jest 19 maja 2025
with open("some_text.txt", mode="r", encoding="utf-8") as file2:
    what_inside = file2.read()
    print(what_inside)
#Ten tekst zastępuje Ala ma kota jest 19 maja

with open("some_text.txt", mode="a", encoding="utf-8") as file2:
    file2.write("Mamy bardzo zimny maj.")
#dodajemy Mamy bardzo zimny maj.
with open("some_text.txt", mode="r", encoding="utf-8") as file2:
    what_inside2 = file2.read()
    print(what_inside2)
#Ten tekst zastępuje Ala ma kota jest 19 majaMamy bardzo zimny maj.