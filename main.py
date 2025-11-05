import random
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


def configure_custom():
    while True:
        user_add = get_maxes("Enter a maximum number for addition, or Enter to skip: ")
        user_sub = get_maxes(
            "Enter a maximum number for subtraction, or Enter to skip: "
        )
        user_mult = get_maxes(
            "Enter a maximum number for multiplication, or Enter to skip: "
        )
        user_div = get_maxes("Enter a maximum number for division, or Enter to skip: ")
        user_sq = get_maxes("Enter a maximum number to square, or Enter to skip: ")
        user_sqrt = get_maxes(
            "Enter a maximum number to square root, or Enter to skip: "
        )
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
        print(Fore.RED + "ERROR: SHOULD NEVER SEE THIS" + Fore.RESET)
        raise SystemExit

    return custom


def play_round(trial, num_q: int, *args: int) -> None:
    errors = 0
    start = time.time()
    for i in range(num_q):
        clear_cons()
        print(Fore.BLUE + f"Question {i + 1}\n" + Fore.RESET)
        errors += trial(*args)
    end = time.time()
    print(
        Fore.BLUE + f"Solved {num_q} problems in {round(end - start, 2)} seconds "
        f"with {errors} error(s)." + Fore.RESET
    )
    print(
        Fore.BLUE
        + f"Average time: {round((end - start) / num_q, 4)} seconds"
        + Fore.RESET
    )


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


def again_msg() -> None:
    print(
        Fore.BLUE
        + "Again? ("
        + Fore.GREEN
        + "y"
        + Fore.RESET
        + "/"
        + Fore.RED
        + "n"
        + Fore.RESET
        + ")"
    )
    return None


def main_loop(*args) -> None:
    again = "y"
    while again == "y":
        play_round(*args)
        again_msg()
        again = input()
        quit_check(again)
        while again.lower() not in {"y", "n", "q"}:
            print(Fore.RED + "Invalid input." + Fore.RESET)
            again_msg()
            again = input()
            quit_check(again)


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
