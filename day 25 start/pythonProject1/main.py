# with open('weather_data.csv') as report:
#     data = report.readlines()
#
#
# import csv
# with open('weather_data.csv') as report:
#     data = csv.reader(report)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))






# data = pandas.read_csv('weather_data.csv')
#
# tem_list = data['temp'].to_list()
# number = len(tem_list)
# sum_of_all = 0
# for i in tem_list:
#     sum_of_all += i
#
# average = sum_of_all /number
# print(f'sum of all temperature = {sum_of_all}')
# print(f'number of days = {number}')
# print(f'average temperature = {average}')
#
# max_value = data['temp'].max()
# print(f'maximum temperature is {max_value}')
# print(data[data.day == 'Monday'])
# print(data[data.temp == max_value])
#
# monday = data[data.day == 'Monday']
# temperature_celsius = monday.temp[0]
# temperature_fahrenheit = (temperature_celsius * 9/5) +32
# print(f'temperature in fahrenheit = {temperature_fahrenheit}')

# dataframe = {
#     'students': ['shirly', 'mathesh', 'kis'],
#     'score': [0, 100, 90],
#     'remarks': ['poor', 'excellent', 'great']
# }
#
# date = pandas.DataFrame(dataframe)
# date.to_csv('new data.csv')


# import pandas as pd
# data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240914.csv')
# color_of_squirrel = data['Primary Fur Color']
# grey = color_of_squirrel == 'Gray'
# cinnamon = color_of_squirrel == 'Cinnamon'
# black = color_of_squirrel == 'Black'
# dataframe =  {
#     'Color': ['Gray', 'Cinnamon', 'Black'],
#     'Count': [grey.sum(), cinnamon.sum(), black.sum()]
#
# }
# color_data = pd.DataFrame(dataframe)
# color_data.to_csv('squirrel count.csv')
# print(color_data)

import turtle
import pandas as pd
screen = turtle.Screen()
screen.title('U. S. game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv('50_states.csv')
states = data['state']
all_states = states.to_list()
guessed_state = []

while  len(guessed_state) < 50:
    answer = screen.textinput(title = f' {len(guessed_state)}/50 Guess the state',
                              prompt = "What's another state name").title()
    if answer == 'Exit':
        missing_state = [state for state in all_states if state not in guessed_state]
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv('missing_state')
        break
    if answer in all_states:
        guessed_state.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        coordinates = data[data.state == answer]
        t.goto(coordinates.x.item(), coordinates.y.item())
        t.write(answer)









screen.exitonclick()

