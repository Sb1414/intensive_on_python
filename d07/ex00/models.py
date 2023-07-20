import random
import json


class VariableMeasurements:
    def __init__(self, respiration, heart_rate, blushing_level, pupillary_dilation):
        self.respiration = respiration
        self.heart_rate = heart_rate
        self.blushing_level = blushing_level
        self.pupillary_dilation = pupillary_dilation


class ReplicantTest:
    def __init__(self, questions_file):
        self.questions_file = questions_file
        self.questions = self.load_questions()
        self.responses = []
        self.score = 0

    def load_questions(self):
        with open(self.questions_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data["questions"]

    def ask_question(self, question):
        print(question["question"])
        for i, response in enumerate(question["responses"], 1):
            print(f"{i}. {response}")
        while True:
            user_input = input("Your response (enter the number): ")
            try:
                user_choice = int(user_input)
                if 1 <= user_choice <= len(question["responses"]):
                    self.responses.append(question["responses"][user_choice - 1])
                    self.score += user_choice
                    break
                else:
                    print("Invalid response. Please select a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def run_test(self):
        for question in self.questions:
            self.ask_question(question)

        while True:
            try:
                respiration = int(input("Частота дыхания (ударов в минуту): "))
                heart_rate = int(input("Частота сердечных сокращений  (Ударов в минуту): "))
                blushing_level = int(input("Уровень покраснения (1-6): "))
                pupillary_dilation = float(input("Расширение зрачков (мм): "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        variable_measurements = VariableMeasurements(respiration, heart_rate, blushing_level, pupillary_dilation)
        return variable_measurements, self.score
