from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
seconds = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps, seconds
    reps = 0
    check_label.config(text='')
    timer_label.config(text='Timer', fg = GREEN)
    window.after_cancel(seconds)
    canvas.itemconfig(timer_text, text='00:00')




# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        timer_label.config(text = 'Break', fg = GREEN)
        counter(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer_label.config(text='Break', fg = PINK)
        counter(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text='Work', fg = RED)
        counter(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def counter(count):
    global reset_timer, seconds
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text =f'{count_min}:{count_sec}')
    if count > 0:
        seconds = window.after(1000, counter, count - 1)
    else:
        global reps
        start_timer()
        mark = ''
        for _ in range(math.floor(reps/2)):
            mark += '✔'
            check_label.config(text = mark)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx = 50, pady = 50, bg = YELLOW)

canvas = Canvas(width = 200,height = 260, bg = YELLOW, highlightthickness = 0)
tomato_image = PhotoImage(file = 'tomato.png')
canvas.create_image(100, 111, image = tomato_image)
timer_text = canvas.create_text(100, 128,text = '00:00', font = (FONT_NAME, 30, 'bold'), fill = 'white')
canvas.grid(column = 1, row = 1)

timer_label = Label(text = 'Timer', font = (FONT_NAME, 44, 'bold'), height = 2, fg = GREEN, bg = YELLOW, highlightthickness = 0)
timer_label.grid(column = 1, row = 0)

start_button = Button(text = 'Start', command = start_timer, width = 10, highlightthickness = 0)
start_button.grid(column = 0, row = 2)

reset_button = Button(text = 'Reset', command = reset,width = 10, highlightthickness = 0)
reset_button.grid(column = 2, row = 2)

check_label = Label( font = (FONT_NAME, 16, 'bold'), height = 3,fg = GREEN, bg = YELLOW, highlightthickness = 0)
check_label.grid(column = 1, row = 3)
window.mainloop()