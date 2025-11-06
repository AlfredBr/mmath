import random
import time
from math import floor, sqrt

from colorama import Fore

from helpers import get_expr, get_int, quit_check


def get_two_rand(top: int) -> tuple[int, int]:
    return (random.randint(2, top), random.randint(2, top))


def addition(top: int) -> tuple[int, float, tuple[str, int, int]]:
    num_wrong = 0
    a = random.randint(1, top)
    b = random.randint(1, top)
    start = time.time()
    ans = get_int(f"{a} + {b} = ")
    while int(ans) != (a + b):
        print(Fore.RED + "--   wrong   --\n" + Fore.RESET)
        num_wrong += 1
        ans = get_int(f"{a} + {b} = ")
    q_time = time.time() - start
    return num_wrong, q_time, ("+", a, b)


def subtraction(top: int) -> tuple[int, float, tuple[str, int, int]]:
    num_wrong = 0
    a = random.randint(1, top)
    b = random.randint(1, top)
    start = time.time()
    ans = get_int(f"{a} - {b} = ")
    while int(ans) != (a - b):
        print(Fore.RED + "--   wrong   --\n" + Fore.RESET)
        num_wrong += 1
        ans = get_int(f"{a} - {b} = ")
    q_time = time.time() - start
    return num_wrong, q_time, ("-", a, b)


def plus_minus(top: int) -> tuple[int, float, tuple[str, int, int]]:
    if random.random() < 0.5:
        return addition(top)
    return subtraction(top)


def multiplication(top: int) -> tuple[int, float, tuple[str, int, int]]:
    num_wrong = 0
    a = random.randint(1, top)
    b = random.randint(1, top)
    start = time.time()
    ans = get_int(f"{a} * {b} = ")
    while int(ans) != (a * b):
        print(Fore.RED + "--   wrong   --\n" + Fore.RESET)
        num_wrong += 1
        ans = get_int(f"{a} * {b} = ")
    q_time = time.time() - start
    return num_wrong, q_time, ("*", a, b)


def times_tables(num: int, top: int) -> tuple[int, float, tuple[str, int, int]]:
    num_wrong = 0
    other_num = random.randint(1, top)
    if random.random() < 0.5:
        a = other_num
        b = num
    else:
        a = num
        b = other_num
    start = time.time()
    ans = get_int(f"{a} * {b} = ", pos=True)
    while ans != (a * b):
        print(Fore.RED + "--   wrong   --\n" + Fore.RESET)
        num_wrong += 1
        ans = get_int(f"{a} * {b} = ", pos=True)
    q_time = time.time() - start
    return num_wrong, q_time, ("*", num, other_num)


def division(top: int) -> tuple[int, float, tuple[str, int, int]]:
    num_wrong = 0
    dividend = random.randint(1, top)
    divisor = random.randint(1, max(floor(dividend / 5), 1))
    print(f"{dividend} / {divisor} = ")
    start = time.time()
    quotient = get_int("Quotient = ")
    remainder = get_int("Remainder = ")
    while (quotient, remainder) != divmod(dividend, divisor):
        print(Fore.RED + "--   wrong   --\n" + Fore.RESET)
        num_wrong += 1
        print(f"{dividend} / {divisor} = ")
        quotient = get_int("Quotient = ")
        remainder = get_int("Remainder = ")
    q_time = time.time() - start
    return num_wrong, q_time, ("/", dividend, divisor)


def square(top: int) -> tuple[int, float, tuple[str, int]]:
    num_wrong = 0
    a = random.randint(1, top)
    start = time.time()
    ans = get_int(f"{a}^2 = ")
    while int(ans) != (a**2):
        print(Fore.RED + "--   wrong   --\n" + Fore.RESET)
        num_wrong += 1
        ans = get_int(f"{a}^2 = ")
    q_time = time.time() - start
    return num_wrong, q_time, ("^", a)


def squareroot(top: int) -> tuple[int, float, tuple[str, int]]:
    TOLERANCE = 0.1
    num_wrong = 0
    a = random.randint(1, top)
    true_root = sqrt(a)
    rounded = round(true_root)
    best_answer = rounded - (rounded**2 - a) / (2 * rounded)
    start = time.time()
    ans = get_expr(f"sqrt({a}) = ")
    while abs(ans - best_answer) > TOLERANCE:
        print(Fore.RED + "--   wrong   --\n" + Fore.RESET)
        num_wrong += 1
        ans = get_expr(f"sqrt({a}) = ")
    q_time = time.time() - start
    print(f"Your answer: {ans}")
    print(f"Best answer: {best_answer}")
    print(f"Actual: {true_root}")
    print(f"Error: {abs(best_answer - true_root)}")
    q = input("Press enter to continue...\n")
    quit_check(q)
    return num_wrong, q_time, ("sqrt", a)


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
