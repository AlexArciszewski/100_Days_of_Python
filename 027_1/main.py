import tkinter

window = tkinter.Tk()
window.title("My First GUI program")
#window #szary pasek

window.minsize(width=800,height=600)


#label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24,"bold"), bg="lightgray") # w nawiasie własciweości labelki
my_label.pack() # side="left",expand=True to umeiszcza labelke na ekranie na srodku left po lewej bootom dól expand to na srodku
#

#zmiana tekstu przez kawargsy jak w słownikach:

my_label["text"] = "Ala ma kota" #inny sposób zmiany textu
my_label.config(text="Ananas")  #jeszcze inny sposób zmiany tekstu


def this_function():
    print("Yeah someone clicked me")
    new_text = input.get()
    my_label["text"] = new_text



#przycisk
button = tkinter.Button(text="YES", command=this_function)
button.pack(side="left")

#input tzw entry


input = tkinter.Entry(width=10)
input.pack()
input.get()
#to co wpiszemy poajwis ie po kliknieciu w przycisk dzieki this_function() w buttonie button



window.mainloop()
#program działa i sradza cy coś sie nie klikneło coś jak while True ale wbudowane
#to nazwsze dajemy na koniec programu