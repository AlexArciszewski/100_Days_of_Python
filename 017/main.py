from question_model import Question #do maina zaciagamiy obiekt question
from data import question_data      #do maina zaciagamiy listę pytan z data.py
from quiz_brain import QuizBrain
question_bank:list = []

for question in question_data:
    question_text:str = question["text"]
    question_answer:str = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your  final score was: {quiz.score}/{len(question_bank)}")