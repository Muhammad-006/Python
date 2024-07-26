from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for i in range(0,len(question_data)):
    question = Question(question_data[i]['text'], question_data[i]['answer'])
    question_bank.append(question)

text = QuizBrain(question_bank)
while text.still_have_questions():
    text.next_question()