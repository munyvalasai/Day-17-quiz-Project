from question_model import Question, QuizBrain
from data import question_data

new_data = []

for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_question = Question(q_text, q_answer)
    new_data.append(new_question)

quiz = QuizBrain(new_data)