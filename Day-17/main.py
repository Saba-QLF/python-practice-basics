from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question = Question(data["text"], data["answer"])
    question_bank.append(question)
quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()
print("You've complete the Quiz.")
print(f"Your final score is {quiz_brain.score}/{quiz_brain.question_number}")