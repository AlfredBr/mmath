import random
import sys
import time

from colorama import Fore

from helpers import (
    addition,
    all_custom,
    clear_cons,
    division,
    get_int,
    multiplication,
    plus_minus,
    square,
    squareroot,
    subtraction,
)


def get_maxes(message: str) -> int | bool:
    while True:
        user_input = input(message).lower().strip()
        if user_input == "q":
            sys.exit()
        elif user_input == "":
            print("Skipping...")
            return False
        try:
            num = int(user_input)
            break
        except ValueError:
            print(
                Fore.RED
                + "Invalid input. Please enter a valid whole number."
                + Fore.RESET
            )
    return num


def configure_custom():
    user_add = get_maxes("Enter a maximum number for addition, or Enter to skip: ")
    user_sub = get_maxes("Enter a maximum number for subtraction, or Enter to skip: ")
    user_mult = get_maxes(
        "Enter a maximum number for multiplication, or Enter to skip: "
    )
    user_div = get_maxes("Enter a maximum number for division, or Enter to skip: ")
    user_sq = get_maxes("Enter a maximum number to square, or Enter to skip: ")
    user_sqrt = get_maxes("Enter a maximum number to square root, or Enter to skip: ")

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
        print(Fore.RED + "Must select at least one operation." + Fore.RESET)
        sys.exit()

    return custom


def play_round(trial, *args: int) -> None:
    print(Fore.BLUE + "How many questions?" + Fore.RESET)
    num_q = get_int(Fore.GREEN + "Enter a number: " + Fore.RESET, pos=True)
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


def main() -> None:
    while True:
        clear_cons()
        operations = ["+", "-", "(+/-)", "*", "/", "^", "sqrt", "custom", "default"]
        operations_str = ", ".join(operations)
        print(
            Fore.BLUE + f"What do you want to practice? ({operations_str})" + Fore.RESET
        )
        op = input(Fore.GREEN + "Operation: " + Fore.RESET)
        op = op.lower().strip()
        if op == "q":
            sys.exit()
        while op not in operations:
            print(
                Fore.RED
                + f"Invalid operation. Please enter a valid operation ({operations})."
                + Fore.RESET
            )
            op = input(Fore.GREEN + "operation: " + Fore.RESET)
            op = op.lower()
            if op == "q":
                sys.exit()
        if op == "custom":
            trial = configure_custom()
            play_round(trial)
        elif op == "default":
            trial = all_custom(999, 999, 99, 999, 99, 99)
            play_round(trial)
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
            play_round(trial, top)
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
        again = input()
        if again == "n":
            sys.exit()


if __name__ == "__main__":
    main()
