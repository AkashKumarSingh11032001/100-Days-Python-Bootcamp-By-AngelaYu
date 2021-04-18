from question_model import Question
from data import question_data

question_bank = []
for quest in question_data:
    q1 = quest["text"]
    ans = quest["answer"]
    new_que = Question(q1,ans)
    question_bank.append(new_que)



