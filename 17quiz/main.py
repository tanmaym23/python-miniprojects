from que import Question 
from data import question_data 
from quiz_brain import quizbrain
q_bank=[]
for questions in question_data:
    q_text=questions["text"]
    q_ans=questions["answer"]
    que1=Question(q_text,q_ans)
    q_bank.append(que1)

quiz=quizbrain(q_bank)
quiz.next_que()