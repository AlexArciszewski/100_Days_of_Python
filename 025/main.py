import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states =[]
states_not_quessed = []
dict_table = {}
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="What's another state name?").title()
    print(answer_state)
    if answer_state == "Exit":
        # for state in all_states:
        #     if state not in guessed_states:
        #         states_not_quessed.append(state)
        states_not_quessed =[state for state in all_states if state not in states_not_quessed]
        table=pd.DataFrame(states_not_quessed,columns=["Missing States"])
        table.to_csv("table.csv", index=False)
        screen.bye()
        break


    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)


turtle.mainloop()




# print(df.head())
#
# writer = turtle.Turtle()
# writer.hideturtle()
# writer.penup()
# game_is_on = True
# states_box = set()
# complete = 0
# tries = 0
# while game_is_on:
#     answer_state = screen.textinput(title=f"{len(states_box)}/50 States Correct",
#         prompt="What's another state name? (or type 'Exit' to quit)")
#     if answer_state.lower() =="exit":
#         break
#
#     elif answer_state.title() in df["state"].values and answer_state.title() not in states_box:
#         states_box.add(answer_state.title())
#         location = df[df['state']== answer_state.title()]
#         x = int(location["x"].values[0])
#         y = int(location["y"].values[0])
#             #print(f"x: {x}, y: {y}")
#         writer.goto(x,y )
#         writer.write(answer_state.title(), font=("Arial", 16, "normal"))
#         tries +=1
#         complete += 1
#     else:
#         print("State not found.")
#         tries += 1
# if len(states_box) == 50:
#     print('Game Over you got all the states')
#     game_is_on = False










# turtle.mainloop()


