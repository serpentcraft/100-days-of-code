# day_17.py — Quiz Game

import requests


# ---------- class Question ----------
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


# ---------- class QuizBrain ----------
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("It's wrong.")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print()


# ---------- getting response from API ----------
url = "https://opentdb.com/api.php?amount=10&category=18&type=boolean"
response = requests.get(url)
api_data = response.json()

html_entities = {
    "&quot;": "'",
    "&#039;": "'",
    "&amp;": "&",
    "&ndash;": "–",
    "&mdash;": "—",
    "&lt;": "<",
    "&gt;": ">",
}


# ---------- Creating Question Bank ----------
question_bank = []

for item in api_data["results"]:
    formatted = item["question"]
    for html, char in html_entities.items():
        formatted = formatted.replace(html, char)
    next_question = Question(formatted, item["correct_answer"])
    question_bank.append(next_question)


# ---------- Starting the Quiz ----------
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
