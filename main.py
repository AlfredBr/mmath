import os
import random
import shutil
import sys
import time
from math import ceil, floor, sqrt

import numexpr


def get_float(message: str) -> float:
    while True:
        user_input = input(message)
        if user_input == "q":
            sys.exit()
        try:
            num = float(user_input)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return num


def get_int(message: str) -> int:
    while True:
        user_input = input(message)
        if user_input == "q":
            sys.exit()
        try:
            num = int(user_input)
            break
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")
    return num


def get_expr(message: str) -> float:
    while True:
        user_input = input(message)
        if user_input == "q":
            sys.exit()
        try:
            num = numexpr.evaluate(user_input)
            num = float(num)
            break
        except Exception:
            print("Invalid input. Please enter a valid whole number.")
    return num


def clear_cons() -> None:
    rows, columns = shutil.get_terminal_size()
    os.system("/usr/bin/clear")  # noqa: S605
    text = "Enter q to quit at any time  "
    print(f"{text:>{rows}}")
    print("\n")


def addition(top: int) -> int:
    num_wrong = 0
    a = random.randint(1, top)
    b = random.randint(1, top)
    ans = get_int(f"{a} + {b} = ")
    while int(ans) != (a + b):
        print("--   wrong  --\n")
        num_wrong += 1
        ans = get_int(f"{a} + {b} = ")
    # print("--  correct --\n")
    return num_wrong


def subtraction(top: int) -> int:
    num_wrong = 0
    a = random.randint(1, top)
    b = random.randint(1, top)
    ans = get_int(f"{a} - {b} = ")
    while int(ans) != (a - b):
        print("--   wrong  --\n")
        num_wrong += 1
        ans = get_int(f"{a} - {b} = ")
    # print("--  correct --\n")
    return num_wrong


def plus_minus(top: int) -> int:
    if random.random() < 0.5:
        return addition(top)
    return subtraction(top)


def multiplication(top: int) -> int:
    num_wrong = 0
    a = random.randint(1, top)
    b = random.randint(1, top)
    ans = get_int(f"{a} * {b} = ")
    while int(ans) != (a * b):
        print("--   wrong  --\n")
        num_wrong += 1
        ans = get_int(f"{a} * {b} = ")
    # print("-- correct --\n")
    return num_wrong


def division(top: int) -> int:
    num_wrong = 0
    dividend = random.randint(1, top)
    divisor = random.randint(1, dividend)
    print(f"{dividend} / {divisor} = ")
    quotient = get_int("Quotient = ")
    remainder = get_int("Remainder = ")
    while (quotient, remainder) != divmod(dividend, divisor):
        print("--   wrong   --\n")
        num_wrong += 1
        print(f"{dividend} / {divisor} = ")
        quotient = get_int("Quotient = ")
        remainder = get_int("Remainder = ")
    # print("-- correct --\n")
    return num_wrong


def square(top: int) -> int:
    num_wrong = 0
    a = random.randint(1, top)
    ans = get_int(f"{a}^2 = ")
    while int(ans) != (a**2):
        print("--   wrong  --\n")
        num_wrong += 1
        ans = get_int(f"{a}^2 = ")
    # print("-- correct --\n")
    return num_wrong


def squareroot(top: int) -> int:
    num_wrong = 0
    a = random.randint(1, top)
    true_root = sqrt(a)
    rounded = round(true_root)
    down = floor(true_root)
    up = ceil(true_root)
    best_answer = rounded - (rounded**2 - a) / (2 * rounded)
    ans = get_expr(f"sqrt({a}) = ")
    while abs(ans - best_answer) > 0.1:
        print("--   wrong  --\n")
        num_wrong += 1
        ans = get_expr(f"sqrt({a}) = ")
    print(f"Best answer: {best_answer}")
    print(f"Actual: {true_root}")
    print(f"Difference: {abs(best_answer - true_root)}")
    q = input("Press enter to continue...\n")
    if q == "q":
        sys.exit()
    return num_wrong


def everything(top: int) -> int:
    num = random.randint(0, 5)
    if num == 0:
        return addition(top)
    if num == 1:
        return subtraction(top)
    if num == 2:
        return multiplication(top)
    if num == 3:
        return division(top)
    if num == 4:
        return square(top)
    return squareroot(top)


def main() -> None:
    clear_cons()
    operations = "+, -, (+/-), *, /, ^, sqrt, all"
    print(f"What do you want to practice? ({operations})")
    op = input("Operation: ")
    if op == "q":
        sys.exit()
    while op not in ["+", "-", "(+/-)", "*", "/", "^", "sqrt", "all"]:
        print(f"Invalid operation. Please enter a valid operation ({operations}).")
        op = input("operation: ")
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
    elif op == "sqrt":
        trial = squareroot
    elif op == "all":
        trial = everything
    else:
        print("Encountered error picking operation. Exiting program...")
        sys.exit()
    print("What is the max number?")
    top = get_int("Enter a number: ")
    print("How many questions?")
    num_q = get_int("Enter a number:")
    errors = 0
    start = time.time()
    for i in range(num_q):
        clear_cons()
        print(f"Question {i + 1}\n")
        errors += trial(top)
    end = time.time()
    print(
        f"Solved {num_q} problems in {round(end - start, 2)} seconds with {errors} error(s)."
    )
    print(f"Average time: {round((end - start) / num_q, 4)} seconds")
    print("Again? (y/n)")
    again = input()
    if again == "y":
        main()
    else:
        sys.exit()


if __name__ == "__main__":
    main()
