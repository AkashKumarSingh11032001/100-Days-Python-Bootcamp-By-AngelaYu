class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list

    def question_left(self):
        if(self.question_number < len(self.question_list)):
            return True
        else:
            return False
    
    def next_question(self):
        current_ques = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {current_ques.text} (True/False) ")
        self.check_ans(user_ans, current_ques.answer)

    def check_ans(self, user_ans, correct_ans):
        if(user_ans.lower() == correct_ans.lower()):
            print("You are Right")
        else:
            print("Wrong")
        print(f"correct ansewer : {correct_ans}")

     
        




    