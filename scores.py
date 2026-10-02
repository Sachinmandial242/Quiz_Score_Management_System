def view_scores():

    print("\n================================")
    print("        PREVIOUS SCORES")
    print("================================")

    try:

        with open("scores.txt", "r") as file:

            data = file.readlines()

            if len(data) == 0:
                print("No scores available.")

            else:
                for line in data:
                    print(line.strip())

    except FileNotFoundError:

        print("No scores available yet.")

    print("================================")


def show_leaderboard():

    print("\n================================")
    print("           LEADERBOARD")
    print("================================")

    try:

        with open("scores.txt", "r") as file:

            data = file.readlines()

        if len(data) == 0:

            print("No scores available.")
            print("Play at least one quiz first.")

        else:

            scores = []

            for line in data:

                line = line.strip()

                if line == "":
                    continue

                parts = line.split("|")

                # New format:
                # Name | Category | Score | Percentage | Grade | Result

                if len(parts) >= 3:

                    name = parts[0].strip()
                    category = parts[1].strip()
                    score_text = parts[2].strip()

                    try:
                        correct = int(score_text.split("/")[0])

                        scores.append(
                            (name, category, correct)
                        )

                    except ValueError:
                        continue

            if len(scores) == 0:

                print("No valid scores found.")

            else:

                # Sort highest score first
                scores.sort(
                    key=lambda x: x[2],
                    reverse=True
                )

                print()

                position = 1

                for name, category, score in scores:

                    print(
                        position,
                        ".",
                        name,
                        "-",
                        category,
                        "-",
                        score,
                        "points"
                    )

                    position = position + 1

    except FileNotFoundError:

        print("No scores available yet.")

    print("================================")