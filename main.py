from questions import questions
from quiz import Quiz
from result import show_result
from scores import view_scores, show_leaderboard


def main():

    while True:

        print("\n==========================================")
        print("     QUIZ & SCORE MANAGEMENT SYSTEM")
        print("==========================================")

        print("1. Start Quiz")
        print("2. View Previous Scores")
        print("3. View Leaderboard")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        # ================= START QUIZ =================

        if choice == "1":

            user_name = input("\nEnter your name: ").strip()

            # Name validation
            if user_name == "":
                print("Name cannot be empty!")
                continue

            print("\nSelect Quiz Category")

            print("1. Python")
            print("2. Data Science")
            print("3. DBMS")

            category_choice = input("Enter category choice: ")

            if category_choice == "1":
                category = "Python"

            elif category_choice == "2":
                category = "Data Science"

            elif category_choice == "3":
                category = "DBMS"

            else:
                print("Invalid category choice!")
                continue

            # Create Quiz object
            quiz = Quiz(questions, user_name, category)

            # Start quiz
            score = quiz.start()

            # Show result
            show_result(
                user_name,
                category,
                score,
                6
            )

        # ================= PREVIOUS SCORES =================

        elif choice == "2":

            view_scores()

        # ================= LEADERBOARD =================

        elif choice == "3":

            show_leaderboard()

        # ================= EXIT =================

        elif choice == "4":

            print("\nThank you for using Quiz & Score Management System!")
            print("Goodbye!")

            break

        else:

            print("\nInvalid choice!")
            print("Please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()