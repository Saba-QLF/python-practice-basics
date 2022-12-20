class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)? : ")
        self.check_answer(user_answer, question.answer)

    def check_answer(self, user_answer, correct_answer):
        if correct_answer == user_answer:
            print(f"you got it right!")
            self.score += 1
        else:
            print(f"That's wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
