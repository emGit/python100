class Brain:

    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def check_answer(self, user_answer, actual_answer):
        if user_answer.lower() == actual_answer.lower():
            print("Correct!")
            self.score += 1
        else: print("Incorrect!")
        print(f"The correct answer was: {actual_answer} ")
        print(f"Your current score is: {self.score}/{self.question_number} ")
        print("\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.check_answer(input(f"Q.{self.question_number} {current_question.text} (True/False): "), current_question.answer)

    def still_has_questions(self): return len(self.question_list) > self.question_number