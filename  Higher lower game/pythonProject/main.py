import random
from flask import Flask
generated_num = random.randint(0,9)

app = Flask(__name__)

@app.route('/')
def title():
    return ('<b><h1>Guess a number between 0 and 9</h1></b>'
            '<img src = https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>')


@app.route('/<int:guess>')
def game(guess):
    if generated_num == guess:
        return ('<b><h1 style = "color:green">You Found Me</h1></b>'
                '<img src = https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>')
    elif generated_num > guess:
        return ('<b><h1 style = "color:red">Too Low</h1></b>'
                '<img src = https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>')
    elif generated_num < guess:
        return ('<b><h1 style = "color:red">Too High</h1></b>'
                '<img src = https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>')




if __name__ == '__main__':
    app.run(debug = True, use_reloader = False)