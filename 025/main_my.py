import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)




df = pd.read_csv("50_states.csv")
print(df.head())

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
game_is_on = True
states_box = set()
complete = 0
tries = 0
while game_is_on:
    answer_state = screen.textinput(title=f"{len(states_box)}/50 States Correct",
        prompt="What's another state name? (or type 'Exit' to quit)")
    if answer_state.lower() =="exit":
        break

    elif answer_state.title() in df["state"].values and answer_state.title() not in states_box:
        states_box.add(answer_state.title())
        location = df[df['state']== answer_state.title()]
        x = int(location["x"].values[0])
        y = int(location["y"].values[0])
            #print(f"x: {x}, y: {y}")
        writer.goto(x,y )
        writer.write(answer_state.title(), font=("Arial", 16, "normal"))
        tries +=1
        complete += 1
    else:
        print("State not found.")
        tries += 1
if len(states_box) == 50:
    print('Game Over you got all the states')
    game_is_on = False










turtle.mainloop()


