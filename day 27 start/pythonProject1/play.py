from tkinter import *
#window
window = Tk()
window.minsize(width = 500, height = 300)
window.title('Mile to Km Converter')
window.config(padx = 150, pady = 20)

#entry_1
entry1 = Entry()
entry1.grid(column = 2, row = 0)



#Label_1
label1 = Label(text = 'Miles', font = ('Times New Roman', 20, 'normal'))
label1.grid(column = 4, row = 0)

#entry_2
label2 = Label(text = '0', font = ('Times New Roman', 20, 'normal'))
label2.grid(column = 2, row = 3)


#Label_2
label3 = Label(text = 'Km', font = ('Times New Roman', 20, 'normal'))
label3.grid(column = 4, row = 3)

#Label_3
label4 = Label(text = 'is equal to', font = ('Times New Roman', 20, 'normal'))
label4.grid(column = 0, row = 3)

#button
def clik_on_calculate():
    miles = float(entry1.get())
    km = round(miles * 1.609)
    label2.config(text = f'{km}')




button = Button(text = 'Calculate', command = clik_on_calculate )
button.grid(column = 2, row = 5)




window.mainloop()
