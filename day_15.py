question_data = [
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "The HTML5 standard was published in 2014.",
        "correct_answer": "True",
        "incorrect_answers": ["False"],
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "The first computer bug was formed by faulty wires.",
        "correct_answer": "False",
        "incorrect_answers": ["True"],
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "FLAC stands for 'Free Lossless Audio Condenser'.",
        "correct_answer": "False",
        "incorrect_answers": ["True"],
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.",
        "correct_answer": "False",
        "incorrect_answers": ["True"],
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "Linus Torvalds created Linux and Git.",
        "correct_answer": "True",
        "incorrect_answers": ["False"],
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "The programming language 'Python' is based off a modified version of 'JavaScript'",
        "correct_answer": "False",
        "incorrect_answers": ["True"],
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "AMD created the first consumer 64-bit processor.",
        "correct_answer": "True",
        "incorrect_answers": ["False"],
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "'HTML' stands for Hypertext Markup Language.",
        "correct_answer": "True",
        "incorrect_answers": ["False"],
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "In most programming languages, the operator ++ is equivalent to the statement '+= 1'.",
        "correct_answer": "True",
        "incorrect_answers": ["False"],
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "hard",
        "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
        "correct_answer": "False",
        "incorrect_answers": ["True"],
    },
]


class Question:
    def __init__(self) -> None:
        self.questions = question_data
        self.index = 0

    def get_question(self):
        if self.index < len(self.questions):
            question = self.questions[self.index]
            setattr(self, "index", self.index + 1)
            return question
        else:
            print("There is no more question")

    def check_answer(self, answer):
        return (
            True
            if self.questions[self.index - 1]["correct_answer"] == answer
            else False
        )


def quiz():
    questions = Question()
    score = 0
    question_count = 0

    while True:
        question = questions.get_question()
        if score == questions.index:
            print("Coagulation you won the game.")
            return

        print(f"This is a {question['difficulty']} lave question")
        answer = input(
            f"Q.{questions.index}: {question['question']} (True/False)? : "
        ).title()
        question_count += 1

        if questions.check_answer(answer):
            score += 1
            print("You got it right!")
            print("The correct answer was:", question["correct_answer"])
            print(f"Your current score is {score}/{question_count}")
            print("\n")
        else:
            print("That's wrong")
            print("The correct answer is:", question["correct_answer"])
            print(f"Your current score is {score}/{question_count}")
            print("\n")

            return None


quiz()
