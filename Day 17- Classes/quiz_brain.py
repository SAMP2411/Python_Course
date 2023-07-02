class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        que = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {que.text} (True/False)?: ")
        self.check_answer(ans, que.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, ans, correct_answer):
        if ans.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your curent score is: {self.score}/{self.question_number}\n")
