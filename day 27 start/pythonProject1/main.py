from tkinter import *

#window
window = Tk()
window.title('first gui program')
window.minsize(width = 500, height= 300)
window.config(padx= 100, pady = 200)


#label
my_label = Label(text = ' My label', font = ('Times New Roman', 18, 'italic'))
my_label.grid(column = 0, row = 0)


#entry
input = Entry(width = 10)
print()
input.grid(column = 3, row = 4)


#button
def input_button():
    my_label.config(text = input.get())
button = Button(text = 'click here', command = input_button)
button.grid(column = 1, row =1)

button2 = Button(text = 'click here')
button2.grid(column = 2, row = 0)


window.mainloop()

