import random
import statistics
import time

from colorama import Fore

from helpers import (
    clear_cons,
    get_int,
    get_maxes,
    quit_check,
)
from operations import (
    addition,
    all_custom,
    division,
    multiplication,
    plus_minus,
    square,
    squareroot,
    subtraction,
    times_tables,
)

ROUNDING_NUM = 2


def configure_custom():
    while True:
        user_add = get_maxes("addition")
        user_sub = get_maxes("subtraction")
        user_mult = get_maxes("multiplication")
        user_div = get_maxes("division")
        user_sq = get_maxes("square")
        user_sqrt = get_maxes("square root")
        if not any([user_add, user_sub, user_mult, user_div, user_sq, user_sqrt]):
            print(Fore.RED + "Error: please specify at least one maximum." + Fore.RESET)
            continue
        break
    options = {
        "add": user_add,
        "sub": user_sub,
        "mult": user_mult,
        "div": user_div,
        "sq": user_sq,
        "sqrt": user_sqrt,
    }

    def custom() -> int:
        top = False
        operation = None
        while not top:
            operation, top = random.choice(list(options.items()))
        if operation == "add":
            return addition(user_add)
        if operation == "sub":
            return subtraction(user_sub)
        if operation == "mult":
            return multiplication(user_mult)
        if operation == "div":
            return division(user_div)
        if operation == "sq":
            return square(user_sq)
        if operation == "sqrt":
            return squareroot(user_sqrt)
        print(
            Fore.RED + "ERROR IN configure_custom(): SHOULD NEVER SEE THIS" + Fore.RESET
        )
        raise SystemExit

    return custom


def play_round(trial, num_q: int, *args: int):
    errors = 0
    q_times = []
    question_log = {}
    start_round = time.time()
    for i in range(num_q):
        clear_cons()
        print(Fore.BLUE + f"Question {i + 1}\n" + Fore.RESET)
        n_errors, q_time, nums = trial(*args)
        errors += n_errors
        q_times.append(round(q_time, ROUNDING_NUM))
        if nums in question_log:
            question_log[nums] = (question_log[nums] + q_time) / 2
        else:
            question_log[nums] = q_time
        clear_cons()
    end_round = time.time()
    clear_cons()
    print(
        Fore.BLUE
        + "Solved "
        + Fore.YELLOW
        + f"{num_q}"
        + Fore.BLUE
        + " problems in "
        + Fore.YELLOW
        + f"{round(end_round - start_round, ROUNDING_NUM)}"
        + Fore.BLUE
        + " seconds with "
        + Fore.YELLOW
        + f"{errors}"
        + Fore.BLUE
        + " error(s).\n"
        + Fore.RESET
    )
    print(
        Fore.BLUE
        + "Average time: \t\t"
        + Fore.YELLOW
        + f"{round(statistics.mean(q_times), ROUNDING_NUM)}"
        + Fore.BLUE
        + " seconds"
        + Fore.RESET
    )
    if len(q_times) > 1:
        print(
            Fore.BLUE
            + "Standard deviation: \t"
            + Fore.YELLOW
            + f"{round(statistics.stdev(q_times), ROUNDING_NUM)}"
            + Fore.BLUE
            + " seconds"
            + Fore.RESET
        )
        print(
            Fore.BLUE
            + "Median time: \t\t"
            + Fore.YELLOW
            + f"{round(statistics.median(q_times), ROUNDING_NUM)}"
            + Fore.BLUE
            + " seconds"
            + Fore.RESET
        )
        print(
            Fore.BLUE
            + "Shortest time: \t\t"
            + Fore.YELLOW
            + f"{round(min(q_times), ROUNDING_NUM)}"
            + Fore.BLUE
            + " seconds."
            + Fore.RESET
        )
        print(
            Fore.BLUE
            + "Longest time: \t\t"
            + Fore.YELLOW
            + f"{round(max(q_times), ROUNDING_NUM)}"
            + Fore.BLUE
            + " seconds."
            + Fore.RESET
        )
        print(
            Fore.BLUE
            + "Range: \t\t\t"
            + Fore.YELLOW
            + f"{round(max(q_times) - min(q_times), ROUNDING_NUM)}"
            + Fore.BLUE
            + " seconds.\n"
            + Fore.RESET
        )
    return question_log


def configure() -> tuple[str, int]:
    operations = [
        "+",
        "-",
        "(+/-)",
        "*",
        "/",
        "^",
        "sqrt",
        "times tables",
        "tt",
        "custom",
        "default",
    ]
    operations_str = ", ".join(operations)
    print(Fore.BLUE + f"What do you want to practice? ({operations_str})" + Fore.RESET)
    op = input(Fore.GREEN + "Operation: " + Fore.RESET)
    op = op.lower().strip()
    quit_check(op)
    while op not in operations:
        print(
            Fore.RED
            + f"Invalid operation. Please enter a valid operation ({operations_str})."
            + Fore.RESET
        )
        op = input(Fore.GREEN + "Operation: " + Fore.RESET)
        op = op.lower()
        quit_check(op)
    print(Fore.BLUE + "How many questions?" + Fore.RESET)
    num_q = get_int(Fore.GREEN + "Enter a number: " + Fore.RESET, pos=True)
    return op, num_q


def print_data(q_log):
    LIMIT = 10
    message = f"\n{Fore.BLUE}Averages:"
    sorted_questions = sorted(q_log.items(), key=lambda item: item[1], reverse=True)
    print(message)
    for op_nums, q_time in sorted_questions[:LIMIT]:
        op, *nums = op_nums
        try:
            a, b = nums
            print(
                Fore.BLUE
                + f"{a}"
                + Fore.YELLOW
                + f" {op} "
                + Fore.BLUE
                + f"{b} | "
                + Fore.GREEN
                + f"{round(q_time, ROUNDING_NUM)} seconds"
                + Fore.RESET
            )
        except ValueError:
            a = nums[0]
            print(
                Fore.BLUE
                + f"{a}"
                + Fore.YELLOW
                + f" {op}"
                + Fore.BLUE
                + " | "
                + Fore.GREEN
                + f"{round(q_time, ROUNDING_NUM)} seconds"
                + Fore.RESET
            )


def again_msg() -> None:
    print(
        "\n"
        + Fore.BLUE
        + "Again? ("
        + Fore.GREEN
        + "y"
        + Fore.BLUE
        + "/"
        + Fore.RED
        + "n"
        + Fore.BLUE
        + f"), or {Fore.YELLOW}d{Fore.BLUE} to view data."
        + Fore.RESET
    )


def main_loop(*args) -> None:
    again = "y"
    while True:
        question_log = play_round(*args)
        while True:
            again_msg()
            again = input().lower().strip()
            quit_check(again)
            if again == "y":
                break
            if again == "n":
                return
            if again == "d":
                print_data(question_log)
            if again not in {"y", "n", "d", "q"}:
                print(Fore.RED + "Invalid input." + Fore.RESET)


def main() -> None:
    while True:
        clear_cons()
        op, num_q = configure()
        if op == "custom":
            trial = configure_custom()
            main_loop(trial, num_q)
        elif op == "default":
            trial = all_custom(999, 999, 99, 999, 99, 99)
            main_loop(trial, num_q)
        elif op in {"times tables", "tt"}:
            trial = times_tables
            print(Fore.BLUE + "Which times table do you want to practice?" + Fore.RESET)
            table_number = get_int(
                Fore.GREEN + "Enter a number: " + Fore.RESET, pos=True
            )
            print(Fore.BLUE + "What number do you want to practice up to?" + Fore.RESET)
            top = get_int(Fore.GREEN + "Enter a number: " + Fore.RESET, pos=True)
            main_loop(trial, num_q, table_number, top)
        else:
            if op == "+":
                trial = addition
            elif op == "-":
                trial = subtraction
            elif op == "(+/-)":
                trial = plus_minus
            elif op == "*":
                trial = multiplication
            elif op == "/":
                trial = division
            elif op == "^":
                trial = square
            else:
                trial = squareroot
            print(Fore.BLUE + "What is the max number?" + Fore.RESET)
            top = get_int(Fore.GREEN + "Enter a number: " + Fore.RESET, pos=True)
            main_loop(trial, num_q, top)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + Fore.BLUE + "Program interrupted. Exiting..." + Fore.RESET)
