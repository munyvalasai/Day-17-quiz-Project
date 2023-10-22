from question_model import Question, QuizBrain
from data import question_data

new_data = []

for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_question = Question(q_text, q_answer)
    new_data.append(new_question)

quiz = QuizBrain(new_data)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_no}")