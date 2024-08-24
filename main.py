import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States Game')

img = 'blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)

data = pd.read_csv('50_states.csv')

def write_state_name(state_name, x, y):
    text_turtle = turtle.Turtle()
    text_turtle.hideturtle()
    text_turtle.penup()
    text_turtle.goto(x, y)
    text_turtle.write(state_name, align="center", font=("Arial", 12, "normal"))

correct_guesses = []
score = 0

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 250)

total_states = 50  # Total number of unique states to guess

while len(correct_guesses) < total_states:
    answer = screen.textinput(
        title="Guess the state",
        prompt="Score: " + str(score) + "\nWhat's another state's name? "
    ).title()

    # Check if the guess is correct and hasn't been guessed before
    if answer in data['state'].values and answer not in correct_guesses:
        state_row = data[data['state'] == answer]
        x = int(state_row['x'])
        y = int(state_row['y'])
        write_state_name(answer, x, y)
        correct_guesses.append(answer)
        score += 1
        score_display.clear()

    elif answer == "Exit":
        missing_states = [state for state in data['state'] if state not in correct_guesses] 
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv') 
        break

# End the game when all 50 states are guessed
screen.textinput(title="Congratulations!", prompt="You've guessed all the states! Press OK to exit.")
screen.bye()
