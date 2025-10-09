import os
import random
import shutil
import sys
from math import sqrt

import numexpr
from colorama import Fore


def get_float(message: str) -> float:
    while True:
        user_input = input(message).lower().strip()
        if user_input == "q":
            sys.exit()
        try:
            num = float(user_input)
            break
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid number." + Fore.RESET)
    return num


def get_int(message: str, pos: bool = False) -> int:
    while True:
        user_input = input(message).lower().strip()
        if user_input == "q":
            sys.exit()
        try:
            num = int(user_input)
            if (num <= 1) & pos:
                print(Fore.RED + "Please enter a number greater than 1." + Fore.RESET)
                continue
            break
        except ValueError:
            print(
                Fore.RED
                + "Invalid input. Please enter a valid whole number."
                + Fore.RESET
            )
    return num


def get_expr(message: str) -> float:
    while True:
        user_input = input(message).lower().strip()
        if user_input == "q":
            sys.exit()
        try:
            num = numexpr.evaluate(user_input)
            num = float(num)
            break
        except Exception:
            print(
                Fore.RED
                + "Invalid input. Please enter a valid whole number."
                + Fore.RESET
            )
    return num


def clear_cons() -> None:
    try:
        rows, columns = shutil.get_terminal_size()
    except Exception:
        rows = 80
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except Exception:
        pass
    text = Fore.CYAN + "Enter q to quit at any time  " + Fore.RESET
    print(Fore.CYAN + f"{text:>{rows}}" + Fore.RESET)
    print("\n")


def addition(top: int) -> int:
    num_wrong = 0
    a = random.randint(1, top)
    b = random.randint(1, top)
    ans = get_int(f"{a} + {b} = ")
    while int(ans) != (a + b):
        print(Fore.RED + "--   wrong   --\n" + Fore.RESET)
        num_wrong += 1
        ans = get_int(f"{a} + {b} = ")
    return num_wrong


def subtraction(top: int) -> int:
    num_wrong = 0
    a = random.randint(1, top)
    b = random.randint(1, top)
    ans = get_int(f"{a} - {b} = ")
    while int(ans) != (a - b):
        print(Fore.RED + "--   wrong   --\n" + Fore.RESET)
        num_wrong += 1
        ans = get_int(f"{a} - {b} = ")
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
        print(Fore.RED + "--   wrong   --\n" + Fore.RESET)
        num_wrong += 1
        ans = get_int(f"{a} * {b} = ")
    return num_wrong


def division(top: int) -> int:
    num_wrong = 0
    dividend = random.randint(1, top)
    divisor = random.randint(1, dividend)
    print(f"{dividend} / {divisor} = ")
    quotient = get_int("Quotient = ")
    remainder = get_int("Remainder = ")
    while (quotient, remainder) != divmod(dividend, divisor):
        print(Fore.RED + "--   wrong   --\n" + Fore.RESET)
        num_wrong += 1
        print(f"{dividend} / {divisor} = ")
        quotient = get_int("Quotient = ")
        remainder = get_int("Remainder = ")
    return num_wrong


def square(top: int) -> int:
    num_wrong = 0
    a = random.randint(1, top)
    ans = get_int(f"{a}^2 = ")
    while int(ans) != (a**2):
        print(Fore.RED + "--   wrong   --\n" + Fore.RESET)
        num_wrong += 1
        ans = get_int(f"{a}^2 = ")
    return num_wrong


def squareroot(top: int) -> int:
    num_wrong = 0
    a = random.randint(1, top)
    true_root = sqrt(a)
    rounded = round(true_root)
    best_answer = rounded - (rounded**2 - a) / (2 * rounded)
    ans = get_expr(f"sqrt({a}) = ")
    while abs(ans - best_answer) > 0.1:
        print(Fore.RED + "--   wrong   --\n" + Fore.RESET)
        num_wrong += 1
        ans = get_expr(f"sqrt({a}) = ")
    print(f"Best answer: {best_answer}")
    print(f"Actual: {true_root}")
    print(f"Difference: {abs(best_answer - true_root)}")
    q = input("Press enter to continue...\n")
    if q == "q":
        sys.exit()
    return num_wrong


def all_custom(
    add_max: int,
    sub_max: int,
    mult_max: int,
    div_max: int,
    square_max: int,
    sqrt_max: int,
):
    def inner():
        num = random.randint(0, 5)
        if num == 0:
            return addition(add_max)
        if num == 1:
            return subtraction(sub_max)
        if num == 2:
            return multiplication(mult_max)
        if num == 3:
            return division(div_max)
        if num == 4:
            return square(square_max)
        return squareroot(sqrt_max)

    return inner
