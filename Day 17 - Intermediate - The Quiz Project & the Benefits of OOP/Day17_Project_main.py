from question_model import Question
from data import question_data
from quize_brain import QuizBrain


question_bank = []
for quest in question_data:
    q1 = quest["text"]
    ans = quest["answer"]
    new_que = Question(q1,ans)
    question_bank.append(new_que)



quize = QuizBrain(question_bank) 
quize.next_question()