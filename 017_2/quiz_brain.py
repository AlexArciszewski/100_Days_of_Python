class QuizBrain:

    def __init__(self, q_list) -> None:
        self.question_number:int = 0    #zmienna z przypisanąw artoscią idzie doselfa ale nie do init'a
        self.question_list: list = q_list #lista jest w init i self
        self.score = 0
    def next_question(self):
        current_question = self.question_list[self.question_number] #pytanie z question bank mające text i answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:{current_question.text}(True/False)")     #text z question_model z obiektu klasy question opdowiadajacy za tekst pytania
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self)-> bool:
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False
        return self.question_number < len(self.question_list)


    def check_answer(self,user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Yaa Man")
        else:
            print("Wrong answer")
        print(f"Correct answer was {correct_answer}")
        print(f"Current score is {self.score}/{self.question_number}")
        print("\n")
