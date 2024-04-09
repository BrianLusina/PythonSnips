from dataclasses import dataclass, field
from typing import Dict, Union, Tuple, List


def parse_options(choices: Dict[str, Union[str, int]]) -> Tuple[str, List[str]]:
    result = ""

    option_keys = [k for k in choices.keys()]

    for select, answer in choices.items():
        result += f"{select}: {answer} \n"

    return result, option_keys


@dataclass
class QuestionOptions:
    question_choices: Dict[str, str]
    points_for_first_guess: int
    points_for_second_guess: int
    question: str
    answer: str
    guess_count: int = field(default=1)
    max_guess_count: int = field(default=2)


def question_logic(question_opts: QuestionOptions) -> int:
    guess_count = question_opts.guess_count
    max_guess_count = question_opts.max_guess_count
    question = question_opts.question
    answer = question_opts.answer
    question_choices = question_opts.question_choices
    points_for_first_guess = question_opts.points_for_first_guess
    points_for_second_guess = question_opts.points_for_second_guess
    points_scored = 0

    print(question)

    question_options, question_keys = parse_options(question_choices)
    print(question_options)

    player_choice = input("Select an answer: ")

    while guess_count <= max_guess_count:
        if player_choice not in question_keys:
            print(f"Kindly select either of these options {question_keys}")
            continue
        else:
            if player_choice == answer:
                if guess_count <= 1:
                    points_scored += points_for_first_guess
                    guess_count += 1
                    break
                elif guess_count == 2:
                    points_scored += points_for_second_guess
                    guess_count += 1
                    break
            else:
                print(
                    f"Selected answer {player_choice} is not correct. Try again. 1 more chance"
                )
                player_choice = input("Select an answer: ")
                guess_count += 1
                continue

    return points_scored


def question_one() -> int:
    question = "What is the capital city of Ethiopia?"
    question_answer = "A"
    question_choices = {
        "A": "Addis Ababa",
        "B": "Nairobi",
        "C": "Eritrea",
        "D": "Djibouti",
        "E": "Namib",
        "F": "Cape Town",
        "G": "Cairo",
        "H": "Kinshasa",
    }

    question_opts = QuestionOptions(
        question=question,
        answer=question_answer,
        question_choices=question_choices,
        points_for_first_guess=2,
        points_for_second_guess=1,
    )

    points_scored = question_logic(question_opts)

    return points_scored


def question_two() -> int:
    question = "Who invented the Mercedes Benz?"
    question_answer = "C"
    question_choices = {
        "A": "German Co.",
        "B": "The Benz Family",
        "C": "Karl Benz",
        "D": "Mercedes Company",
        "E": "Volkswagen",
        "F": "Karl Volvo",
        "G": "Unknown",
        "H": "Reminisce Gasmotorenfabrik",
    }

    question_opts = QuestionOptions(
        question=question,
        answer=question_answer,
        question_choices=question_choices,
        points_for_first_guess=3,
        points_for_second_guess=2,
    )

    points_scored = question_logic(question_opts)

    return points_scored


def question_three() -> int:
    question = "What is the capital city of Ethiopia?"

    question_answer = "A"
    question_choices = {
        "A": "Addis Ababa",
        "B": "Nairobi",
        "C": "Eritrea",
        "D": "Djibouti",
        "E": "Namib",
        "F": "Cape Town",
        "G": "Cairo",
        "H": "Kinshasa",
    }

    question_opts = QuestionOptions(
        question=question,
        answer=question_answer,
        question_choices=question_choices,
        points_for_first_guess=4,
        points_for_second_guess=3,
    )

    points_scored = question_logic(question_opts)

    return points_scored


if __name__ == "__main__":
    title = "Guess Game"
    total_points = 0

    print(
        f"\nWelcome to the {title}. For each question, you have a maximum of 2 guesses. If you get the first guess correctly, "
        f"You score maximum points, if you guess it wrong you have 1 more chance, but with fewer points, either way"
        f"you proceed to the next question\n"
    )

    print("-----" * 10)
    print("Question 1:")
    question_one_points = question_one()
    total_points += question_one_points
    print(f"Points so far: {total_points}")

    print("-----" * 10)
    print("Question 2:")
    question_two_points = question_two()
    total_points += question_two_points
    print(f"Points so far: {total_points}")

    print("-----" * 10)
    print("Question 3:")
    question_three_points = question_three()
    total_points += question_three_points

    print("-----" * 10)
    print(f"Total points you have scored: {total_points}/9")
    print(f"Thank you for playing the {title}!")
    print("-----" * 10)
