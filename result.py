def show_result(user_name, category, score, total_questions):

    percentage = (score / total_questions) * 100

    if percentage >= 80:
        grade = "A"

    elif percentage >= 60:
        grade = "B"

    elif percentage >= 40:
        grade = "C"

    else:
        grade = "D"

    if percentage >= 40:
        result = "PASS"

    else:
        result = "FAIL"

    print("\n================================")
    print("           QUIZ RESULT")
    print("================================")

    print("Name       :", user_name)
    print("Category   :", category)
    print("Questions  :", total_questions)
    print("Correct    :", score)
    print("Wrong      :", total_questions - score)
    print("Score      :", score, "/", total_questions)
    print("Percentage :", round(percentage, 2), "%")
    print("Grade      :", grade)
    print("Result     :", result)

    print("================================")

    # Save result
    with open("scores.txt", "a") as file:

        file.write(
            user_name + " | " +
            category + " | " +
            str(score) + "/" + str(total_questions) + " | " +
            str(round(percentage, 2)) + "% | Grade " +
            grade + " | " + result + "\n"
        )

    print("Result saved successfully!")