class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    def still_have_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    def next_question(self):
        this_question = self.question_list[(self.question_number)]
        self.question_number += 1
        guess = input(f"Q.{self.question_number}: "
                           f"{this_question.text}. "
                           f"(True/False)? ")
        self.check_for_true(this_question.answer, guess)
    def check_for_true(self, answer, guess):
        if answer == guess:
            self.score += 1
            print("You got it right!")
            print(f'The correct answer was: {answer}.')
            print(f'Your current score is {self.score}/{self.question_number}\n')
        else:
            print("That's wrong!")
            print(f'The correct answer was: {answer}.')
            print(f'Your current score is {self.score}/{self.question_number}\n')
            exit()
