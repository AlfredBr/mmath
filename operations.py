import random
import time
from math import floor, sqrt

from colorama import Fore

from utils import get_expr, get_int, quit_check

##################################################################################################
# These should all be functions that take a single input,
# the maximum number you are asked to compute.
# They should input a single random question to the screen, time how long it
# takes to answer that question correctly, and track how many mistakes.
# They should return the number of errors, the time for the question,
# and a tuple that contains the operation symbol and the numbers asked.
# Special cases can be given a specific config function in config.py
#
# Be sure to add new functions to the ALL_OPERATIONS dictionary in config.py
##################################################################################################


def addition(top: int) -> tuple[int, float, tuple[str, int, int]]:
    num_wrong: int = 0
    a: int = random.randint(1, top)
    b: int = random.randint(1, top)
    start: float = time.time()
    ans: int = get_int(f"{a} + {b} = ")
    while ans != (a + b):
        print(Fore.RED + "--   wrong   --\n" + Fore.RESET)
        num_wrong += 1
        ans = get_int(f"{a} + {b} = ")
    q_time: float = time.time() - start
    return num_wrong, q_time, ("+", a, b)


def subtraction(top: int) -> tuple[int, float, tuple[str, int, int]]:
    num_wrong: int = 0
    a: int = random.randint(1, top)
    b: int = random.randint(1, top)
    start: float = time.time()
    ans: int = get_int(f"{a} - {b} = ")
    while ans != (a - b):
        print(Fore.RED + "--   wrong   --\n" + Fore.RESET)
        num_wrong += 1
        ans = get_int(f"{a} - {b} = ")
    q_time: float = time.time() - start
    return num_wrong, q_time, ("-", a, b)


def plus_minus(top: int) -> tuple[int, float, tuple[str, int, int]]:
    if random.random() < 0.5:
        return addition(top)
    return subtraction(top)


def multiplication(top: int) -> tuple[int, float, tuple[str, int, int]]:
    num_wrong: int = 0
    a: int = random.randint(1, top)
    b: int = random.randint(1, top)
    start: float = time.time()
    ans: int = get_int(f"{a} * {b} = ")
    while ans != (a * b):
        print(Fore.RED + "--   wrong   --\n" + Fore.RESET)
        num_wrong += 1
        ans = get_int(f"{a} * {b} = ")
    q_time: float = time.time() - start
    return num_wrong, q_time, ("*", a, b)


def times_tables(top: int, num: int) -> tuple[int, float, tuple[str, int, int]]:
    num_wrong: int = 0
    other_num: int = random.randint(1, top)
    if random.random() < 0.5:
        a: int = num
        b: int = other_num
    else:
        a: int = other_num
        b: int = num
    start: float = time.time()
    ans: int = get_int(f"{a} * {b} = ", pos=True)
    while ans != (a * b):
        print(Fore.RED + "--   wrong   --\n" + Fore.RESET)
        num_wrong += 1
        ans = get_int(f"{a} * {b} = ", pos=True)
    q_time: float = time.time() - start
    return num_wrong, q_time, ("*", num, other_num)


# Defines what the maximum divisor will be. A value of 5 makes the largest divisor
# one-fifth of the dividend.
DIVISOR_MAX: int = 5


def division(top: int) -> tuple[int, float, tuple[str, int, int]]:
    num_wrong: int = 0
    dividend: int = random.randint(1, top)
    divisor: int = random.randint(1, max(floor(dividend / DIVISOR_MAX), 1))
    print(f"{dividend} / {divisor} = ")
    start: float = time.time()
    quotient: int = get_int("Quotient = ")
    remainder: int = get_int("Remainder = ")
    while (quotient, remainder) != divmod(dividend, divisor):
        print(Fore.RED + "--   wrong   --\n" + Fore.RESET)
        num_wrong += 1
        print(f"{dividend} / {divisor} = ")
        quotient = get_int("Quotient = ")
        remainder = get_int("Remainder = ")
    q_time: float = time.time() - start
    return num_wrong, q_time, ("/", dividend, divisor)


def square(top: int) -> tuple[int, float, tuple[str, int]]:
    num_wrong: int = 0
    a: int = random.randint(1, top)
    start: float = time.time()
    ans: int = get_int(f"{a}^2 = ")
    while int(ans) != (a**2):
        print(Fore.RED + "--   wrong   --\n" + Fore.RESET)
        num_wrong += 1
        ans = get_int(f"{a}^2 = ")
    q_time: float = time.time() - start
    return num_wrong, q_time, ("^", a)


######################################################
# defines how close a guess has to be for squareroot()
# a value of 0.01 means that an answer has to be within 1%
# of the true root to be correct
TOLERANCE: float = 0.01


def squareroot(top: int) -> tuple[int, float, tuple[str, int]]:
    num_wrong: int = 0
    a: int = random.randint(1, top)
    true_root: float = sqrt(a)
    rounded: int = round(true_root)
    best_answer: float = rounded - (rounded**2 - a) / (2 * rounded)
    tol = best_answer * TOLERANCE
    correct_range = (
        min(true_root - tol, best_answer - tol),
        max(true_root + tol, best_answer + tol),
    )
    start: float = time.time()
    ans: float = get_expr(f"sqrt({a}) = ")
    while (ans < correct_range[0]) or (ans > correct_range[1]):
        print(Fore.RED + "--   wrong   --\n" + Fore.RESET)
        num_wrong += 1
        ans = get_expr(f"sqrt({a}) = ")
    q_time: float = time.time() - start
    print()
    print(
        f"{Fore.BLUE}{'Newton\'s method approximation:':<30} {Fore.YELLOW}{best_answer}{Fore.RESET}"
    )
    print(f"{Fore.BLUE}{'Range:':<30} {Fore.YELLOW}{correct_range}{Fore.RESET}")
    print(f"{Fore.BLUE}{'Actual:':<30} {Fore.YELLOW}{true_root}{Fore.RESET}")
    print(
        f"{Fore.BLUE}{'Difference:':<30} {Fore.YELLOW}{abs(best_answer - true_root)}{Fore.RESET}"
    )
    q: str = (
        input(Fore.GREEN + "Press enter to continue...\n" + Fore.RESET).strip().lower()
    )
    quit_check(q)
    return num_wrong, q_time, ("sqrt", a)


def print_complex_number(a: int, b: int) -> str:
    if b > 0:
        return f"{a} + {b}i"
    return f"{a} - {abs(b)}i"


def complex_multiplication(top: int):
    num_wrong: int = 0
    a: int = random.randint(-1 * top, top)
    b: int = random.randint(-1 * top, top)
    c: int = random.randint(-1 * top, top)
    d: int = random.randint(-1 * top, top)
    print(f"({print_complex_number(a, b)}) * ({print_complex_number(c, d)}) = ")
    start: float = time.time()
    real_part_ans: int = get_int("Real = ")
    imaj_part_ans: int = get_int("Imaj = ")
    while (real_part_ans, imaj_part_ans) != (a * c - b * d, a * d + b * c):
        print(Fore.RED + "--   wrong   --\n" + Fore.RESET)
        num_wrong += 1
        print(f"({print_complex_number(a, b)}) * ({print_complex_number(c, d)}) = ")
        real_part_ans: int = get_int("Real = ")
        imaj_part_ans: int = get_int("Imaj = ")
    q_time: float = time.time() - start
    return (
        num_wrong,
        q_time,
        ("*", f"({print_complex_number(a, b)})", f"({print_complex_number(c, d)})"),
    )


def default():
    def inner():
        num = random.randint(0, 5)
        if num == 0:
            return addition(999)
        if num == 1:
            return subtraction(999)
        if num == 2:
            return multiplication(99)
        if num == 3:
            return division(999)
        if num == 4:
            return square(99)
        return squareroot(99)

    return inner
