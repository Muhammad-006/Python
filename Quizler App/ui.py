from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Quiz_interfece:
    def __init__(self, quiz_obj: QuizBrain):
        self.quiz_text = quiz_obj
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg = THEME_COLOR, padx = 20, pady = 20)

        self.score_label = Label(text = 'Score: 0',
                                 highlightthickness = 0, bg = THEME_COLOR, fg = 'white')
        self.score_label.grid(column = 1, row = 0)

        self.canvas = Canvas(width = 300, height = 250, bg = 'white')
        self.this_question = self.canvas.create_text(150, 125,
                                text = 'I love Eyman Shafiq.', width = 260,
                                font = ('Arial', 18, 'italic'), fill = THEME_COLOR)
        self.canvas.grid(column = 0, row = 1, columnspan = 2, sticky = 'ew', pady = 50)

        true_image = PhotoImage(file = "images/true.png")
        self.true_button = Button(image = true_image,highlightthickness = 0,
                                  bg = THEME_COLOR, pady= 20,
                                  command = self.checked_true)
        self.true_button.grid(column = 0, row = 2)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0,
                                  bg=THEME_COLOR, pady= 20,
                                  command = self.checked_false)
        self.false_button.grid(column = 1, row = 2)

        self.quiz_next_question()

        self.window.mainloop()

    def quiz_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz_text.still_has_questions():
            new_question = self.quiz_text.next_question()
            self.canvas.itemconfig(self.this_question, text = new_question)
        else:
            self.canvas.itemconfig(self.this_question, text = "You have reached the end of the quiz.")
            self.true_button.config(state = 'disabled')
            self.false_button.config(state = 'disabled')


    def checked_true(self):
        true_or_false = self.quiz_text.check_answer("true")
        if true_or_false:
            self.canvas.config(bg = 'Lime')
            self.score_label.config(text=f"Score: {self.quiz_text.score}")
        else:
            self.canvas.config(bg = 'red')
        self.window.after(1000, self.quiz_next_question)

    def checked_false(self):
        true_or_false = self.quiz_text.check_answer("false")
        if true_or_false:
            self.canvas.config(bg = 'Lime')
            self.score_label.config(text=f"Score: {self.quiz_text.score}")
        else:
            self.canvas.config(bg = 'red')
        self.window.after(1000, self.quiz_next_question)

