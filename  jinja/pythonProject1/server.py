from http.client import responses

import requests

from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def welcome():
    return ('<h1>Welcome to age_gender prediction</h1>'
            '<h2>Enter your name on the url</h2>')



@app.route('/<names>')
def result(names):
    name = names.capitalize()
    params = {
        'name': names
    }
    gender_api = requests.get(url='https://api.genderize.io', params=params)
    dic = gender_api.json()
    gender = dic['gender'].capitalize()

    parameters = {
        'name': names
    }

    age_api = requests.get(url='https://api.agify.io', params=parameters)
    diction = age_api.json()
    age = diction['age']
    return render_template('index.html', input_name = name, user_gender= gender,user_age = age)


@app.route('/blog')
def blog():
    blog_url = ' https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_post = response.json()
    return render_template('blog.html', post = all_post)



if __name__ == '__main__':
    app.run(debug=True)


print('Congrats you have completed the challenge')

