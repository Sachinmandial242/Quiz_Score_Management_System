import random


class Quiz:

    def __init__(self, questions, user_name, category):
        self.questions = questions
        self.user_name = user_name
        self.category = category
        self.score = 0

    def start(self):

        # Select questions according to category
        selected_questions = []

        for question in self.questions:
            if question["category"] == self.category:
                selected_questions.append(question)

        # Shuffle questions
        random.shuffle(selected_questions)

        print("\n================================")
        print("          QUIZ STARTED")
        print("================================")

        print("Player  :", self.user_name)
        print("Category:", self.category)
        print("Total Questions:", len(selected_questions))

        for i, question in enumerate(selected_questions, start=1):

            print("\nQ", i, ".", question["question"])

            print("A.", question["options"][0])
            print("B.", question["options"][1])
            print("C.", question["options"][2])
            print("D.", question["options"][3])

            # Input validation
            while True:

                answer = input("Enter your answer (A/B/C/D): ").upper()

                if answer in ["A", "B", "C", "D"]:
                    break

                print("Invalid input! Please enter A, B, C or D.")

            if answer == question["answer"]:

                print("Correct Answer!")
                self.score = self.score + 1

            else:

                print("Wrong Answer!")
                print("Correct answer is:", question["answer"])

        return self.score