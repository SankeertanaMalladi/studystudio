def generate_plan(subject, performance):

    if performance == "Excellent":

        return [

            f"Revise advanced {subject} concepts",

            "Solve 20 practice questions",

            "Complete one mini project",

            "Read official documentation",

            "Take another assessment"

        ]

    elif performance == "Good":

        return [

            f"Revise intermediate {subject} concepts",

            "Practice coding exercises",

            "Read study resources",

            "Solve 15 MCQs",

            "Review mistakes"

        ]

    elif performance == "Average":

        return [

            f"Study the basics of {subject}",

            "Read beginner tutorials",

            "Practice easy exercises",

            "Solve 10 MCQs",

            "Revise every day"

        ]

    else:

        return [

            f"Start learning {subject} from scratch",

            "Read beginner notes",

            "Practice simple examples",

            "Study for one hour daily",

            "Retake the quiz after revision"

        ]