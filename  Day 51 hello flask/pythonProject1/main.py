

from flask import Flask

# app = Flask(__name__)
#
# # @app.route('/')
# # def hello_world():
# #     return ('<h1 style = "text-align: center">Hello, World!</h1>'
# #             '<p>This is a paragraph</p>'
# #             '<img src = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnVmajBhZ3c4eXk4czR2Y2I2M3o4YWR2dm1sNXE0YW92bDY4MW13MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/GeimqsH0TLDt4tScGw/giphy.gif" width =200>')
#
# def make_bold(function):
#     def text_bold():
#         return "<b>" + function() + "</b>"
#
#     return text_bold
#
# def make_italic(function):
#     def text_italic():
#         return "<em>" + function() + "</em>"
#     return text_italic
#
# def make_line(function):
#     def text_line():
#         return "<u>" + function() + "</u>"
#     return text_line
#
# @app.route('/')
# @make_bold
# @make_italic
# @make_line
# def greet():
#     return 'Hello there'
#
# if __name__ == '__main__':
#     app.run(debug = True)

class User:

    def __init__(self,name):
        self.name = names
        self.is_logged_in = False


def decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])

    return wrapper


@decorator
def welcome(user):
    print(f'Welcome to {user.name} blog post')


new = User('jhon')
new.is_logged_in = True
welcome(new)
