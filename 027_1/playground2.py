from tkinter import *

def this_function():
    print("Yeah someone clicked me")
    new_text = input.get()
    #my_label["text"] = new_text
    my_label.config(text=new_text)

def that_function():
    print("Yeah someone clecked me also")
    my_label.config(text="new button is awesome")


window = Tk()
window.title("My First GUI program")
#window #szary pasek
window.minsize(width=800,height=600)
#padding?
window.config(padx=100, pady=100)


#label
my_label = Label(text="I am a label", font=("Arial", 24,"bold"), bg="lightgray") # w nawiasie własciweości labelki
#my_label.pack() # side="left",expand=True to umeiszcza labelke na ekranie na srodku left po lewej bootom dól expand to na srodku
my_label.config(text="NEW TEXT BABY")

#zmiana tekstu przez kawargsy jak w słownikach:

my_label["text"] = "Ala ma kota" #inny sposób zmiany textu
my_label.config(text="Ananas")  #jeszcze inny sposób zmiany tekstu
#my_label.place(x=0,y=0) #ustawiamy nawiaz w punkcie w lewym górnym rogu
my_label.grid(column=0, row=0)







#przycisk
button = Button(text="YES", command=this_function)
#button.pack(side="left")
button.grid(column=2, row=2)
#input tzw entry


new_button = Button(text="I'm the New Button Baby", command=that_function)
new_button.grid(column=3,row=1)


input = Entry(width=10)
#input.pack()
input.get()
#to co wpiszemy poajwis ie po kliknieciu w przycisk dzieki this_function() w buttonie button
input.grid(column=4, row=3)



window.mainloop()
#program działa i sradza cy coś sie nie klikneło coś jak while True ale wbudowane
#to nazwsze dajemy na koniec programu

#uzywamy albo pack albo grid