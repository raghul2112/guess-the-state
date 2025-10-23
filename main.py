import turtle
import pandas

screen=turtle.Screen()
turtle=turtle.Turtle()
screen.title("US State Game")
image="./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.bgpic(image)
turtle.hideturtle()
turtle.penup()
# user_input=screen.textinput(title="Guess the Statte",prompt="what's another stat name?")
data=pandas.read_csv("50_states.csv")
# data_list=data.state.to_list() #convert pandas DataFram into list
# print(data_list)
# if user_input.title() in data.state.values:#this is a anothe method to convert pandas DataFrame in to list
#     print("hai")
#     print(user_input)
#
# row=data[data.state==user_input]
# print(row)
all_state=data.state.to_list()
game_is_on=True
ans=0
guess_state=[]
while game_is_on:
    user_input = (screen.textinput(title=f"{ans}/50 Guess the Statte", prompt="what's another stat name?")).title()

    if user_input in data.state.values:
        if user_input not in guess_state:
            guess_state.append(user_input)
            ans += 1
        row = data[data.state == user_input]
        turtle.goto(int(row['x'].values[0]),int(row['y'].values[0]))
        turtle.write(user_input)
        if ans==50:
            game_is_on=False
    if user_input=="Exit":
        missing_state=[]
        for state in all_state:
            if state not in guess_state:
                missing_state.append(state)
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("missing_state.csv")

        break




