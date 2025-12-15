import pandas as pd
from turtle import Turtle,Screen

turtle = Turtle()
sc = Screen()

sc.title("US State Game")
img_add = "blank_states_img.gif"
sc.addshape(img_add)
turtle.shape(img_add)

data = pd.read_csv("50_states.csv")
data_state = data.state.to_list()   
guessed_state = []

while len(guessed_state) < 50:
    ans_states = sc.textinput(f"{len(guessed_state)}/50 Guess the State", "What's the Another States Name?").title()    
    if ans_states == "Exit":
        missing_states = []
        for state in data_state:
            if state not in guessed_state:
                missing_states.append(state)
        print(missing_states)
        break
    if ans_states in data_state:
        guessed_state.append(ans_states)
        state_cor = data[data.state == ans_states]
        new_turtle = Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(state_cor.x.item(),state_cor.y.item())
        new_turtle.write(ans_states)
    




#def get_the_mouse_click_coor(x,y):
#    print(x,y)
#turtle.onscreenclick(get_the_mouse_click_coor)
#turtle.mainloop()

sc.exitonclick()