from tkinter import *


def kilometer():
    miles = float(put.get())
    kilo_meter = round(miles * 1.609344, 2)
    answer.config(text = f'{kilo_meter}', font = ('Courier', 16))


window = Tk()
window.minsize(500, 600)
window.title('Miles to Kilometer GUI')
window.config(padx = 50, pady = 50)

put = Entry(width = 15)
put.grid(column = 1, row = 0)
put.get()

write = Label(text = 'Miles', font = ('Courier', 16))
write.grid(column = 2, row = 0)

another = Label(text ='is equal to ', font = ('Courier', 16))
another.grid(column = 0, row = 1)

answer = Label(text = '')
answer.grid(column = 1, row = 1)

kilo = Label(text ='kilos.', font = ('Courier', 16))
kilo.grid(column = 2, row = 1)

button = Button(text = "Calculate", command = kilometer, font = ('Courier', 16, 'bold'))
button.grid(column = 1, row = 3)

window.mainloop()