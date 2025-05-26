from tkinter import *


#Program window
program_window = Tk()
program_window.title("Mile to Km Converter")
program_window.minsize(width=360, height=240)
program_window.config(padx=40, pady=40)

#Mile input
mile_input = Entry(width=5)
mile_input.get()
mile_input.grid(column=3, row=2)
mile_input.focus() #cursor

#label is equal to
is_iqual_to_label = Label(text="Is equal to: ",font=("Arial", 20,"bold"))
is_iqual_to_label.grid(column=2, row=3)

#Miles label
miles_label = Label(text="Miles",font=("Arial", 20,"bold"))
miles_label.grid(column=6, row=2)

#Km label
km_label = Label(text="Km",font=("Arial", 20,"bold"))
km_label.grid(column=6, row=3)


#result label
res_label = Label(text=" ",font=("Arial", 20,"bold"))
res_label.grid(column=3, row=3)


#calculator
def calculator():
    miles_value = mile_input.get()
    km_value = float(miles_value) * 1.609
    km_value = round(km_value, 2)
    res_label.config(text=km_value)


#button
calc_button = Button(text="Calculate", command=calculator)
calc_button.grid(column=3,row=4)


program_window.mainloop()