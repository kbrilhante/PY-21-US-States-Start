import turtle as t
import pandas as pd

def write_state(state_name, pos_x, pos_y):
    global writer
    writer.goto(pos_x, pos_y)
    writer.write(arg=state_name, align="center", font=("Verdana", 10, "normal"))

scr = t.Screen()
scr.title('US States Game')
scr.setup(725, 491)
image = 'blank_states_img.gif'
scr.addshape(image)

data = pd.read_csv('50_states.csv')

t.shape(image)
writer = t.Turtle()
writer.speed("fastest")
writer.hideturtle()
writer.penup()

# def get_mouse_click_coor(x, y):
#     print(x, y)
# t.onscreenclick(get_mouse_click_coor)

# states = data.state.to_list()
# for state in states:
#     info = check_answer(state)
#     write_state(state, info.x.item(), info.y.item())

correct_answers = []
while len(correct_answers) < 50:
    answer_state = scr.textinput(title=f"{len(correct_answers)} / 50 States Correct", prompt="Guess a State").title()
    result = data[data.state == answer_state]
    if len(result) > 0 and answer_state not in correct_answers:
        correct_answers.append(answer_state)
        write_state(answer_state, result.x.item(), result.y.item())

scr.mainloop()