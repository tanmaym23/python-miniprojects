from main import q_text
class quizbrain:
    def __init__(self,q_list):
        self.question_no=0
        self.question_list=q_list

    def next_que(self):
        current_que=self.question_list[self.question_no]
        input(f"q{self.question_no}:{self.q_text} (t/f)")