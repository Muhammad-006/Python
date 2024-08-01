from turtle import Turtle,Screen
import turtle
import pandas

IMAGE_PATH = 'blank_states_img.gif'
states_guessed = []

screen = Screen()
screen.setup(740,520)
screen.title('Us-States')
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

data = pandas.read_csv('50_states.csv')
name_of_states = data['state'].to_list()

while len(states_guessed) < 50:
    guess = screen.textinput(title = f'{len(states_guessed)}/50 States Correct'
                             , prompt = "What's another state?").title()

    if guess == 'Exit':
        break
    if guess not in states_guessed and guess in name_of_states:
        record = data[data.state == guess]
        x = record.x.item()
        y = record.y.item()
        place = Turtle()
        place.hideturtle()
        place.penup()
        place.goto(x, y)
        place.write(f'{guess}')
        states_guessed.append(guess)

for current_state in states_guessed:
    name_of_states.remove(current_state)

csv_dict = {
    'States Not Guessed': name_of_states
}
convert = pandas.DataFrame(csv_dict)
convert.to_csv('States to learn.csv')
