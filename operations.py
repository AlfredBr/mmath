import random
from math import floor, sqrt

from colorama import Fore

from helpers import get_expr, get_int, quit_check


def get_two_rand(top: int) -> tuple[int, int]:
    return (random.randint(2, top), random.randint(2, top))


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


def times_tables(num: int, top: int) -> int:
    num_wrong = 0
    if random.random() < 0.5:
        a = random.randint(1, top)
        b = num
    else:
        a = num
        b = random.randint(1, top)
    ans = get_int(f"{a} * {b} = ", pos=True)
    while ans != (a * b):
        print(Fore.RED + "--   wrong   --\n" + Fore.RESET)
        num_wrong += 1
        ans = get_int(f"{a} * {b} = ", pos=True)
    return num_wrong


def division(top: int) -> int:
    num_wrong = 0
    dividend = random.randint(1, top)
    divisor = random.randint(1, max(floor(dividend / 5), 1))
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
    print(f"Your answer: {ans}")
    print(f"Best answer: {best_answer}")
    print(f"Actual: {true_root}")
    print(f"Error: {abs(best_answer - true_root)}")
    q = input("Press enter to continue...\n")
    quit_check(q)
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
