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

while quize.question_left():
    quize.next_question()

print("You completed the Quize Challlenge\n")
print(f"Your final score {quize.score}/{quize.question_number}")
