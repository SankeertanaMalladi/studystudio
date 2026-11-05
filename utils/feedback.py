def generate_feedback(performance, quiz_score):

    feedback = []

    if performance == "Excellent":

        feedback.append(
            "Excellent work! You have a strong understanding of this subject."
        )

        feedback.append(
            "Try solving advanced problems to improve further."
        )

    elif performance == "Good":

        feedback.append(
            "Good job! Your fundamentals are clear."
        )

        feedback.append(
            "Practice a few more questions to reach an excellent level."
        )

    elif performance == "Average":

        feedback.append(
            "You understand the basics but need more practice."
        )

        feedback.append(
            "Spend more time revising important concepts."
        )

    else:

        feedback.append(
            "You need to strengthen your basics."
        )

        feedback.append(
            "Start from beginner topics before attempting advanced concepts."
        )

    feedback.append(
        f"Your Quiz Score is {quiz_score}%."
    )

    return feedback