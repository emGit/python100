from question_model import Question
from quiz_brain import Brain
from data import question_data
questions = []
for i in question_data: questions.append(Question(i["text"], i["answer"]))
brain = Brain(questions)
while brain.still_has_questions(): brain.next_question()
print("You have completed the quiz.")
print(f"Your final score is: {brain.score}/{len(questions)}")