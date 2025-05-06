

class Question:


    def __init__(self, q_text: str, q_answer:str):
        self.text = q_text    #q_text z lewej musi być taki sam jak w print(new_q.q_text)
        self.answer = q_answer


def main() -> None:
    new_q = Question("Alamakota","True")
    print(new_q.text)



if __name__ == "__main__":
    main()