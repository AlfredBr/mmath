import datetime
import random
import time
from collections.abc import Callable
from dataclasses import dataclass
from math import floor, sqrt

from colorama import Fore

from utils import get_day, get_expr, get_int, quit_check

##################################################################################################
# These should all be functions that take a single input,
# the maximum number you are asked to compute.
# They should input a single random question to the screen, time how long it
# takes to answer that question correctly, and track how many mistakes.
# They should all return a QuestionResult object.
# Special cases can be given a specific config function in config.py
#
# Be sure to add new functions to the ALL_OPERATIONS dictionary in config.py
##################################################################################################


@dataclass
class QuestionResult:
    num_wrong: int
    question_time: float
    question_info: tuple[str, str, str] | tuple[str, str]


def wrong() -> int:
    print(f"{Fore.RED}--   wrong   --\n{Fore.RESET}")
    return 1


def addition(top: int) -> QuestionResult:
    num_wrong: int = 0
    a: int = random.randint(1, top)
    b: int = random.randint(1, top)
    start: float = time.time()
    ans: int = get_int(f"{a} + {b} = ")
    while ans != (a + b):
        num_wrong += wrong()
        ans = get_int(f"{a} + {b} = ")
    q_time: float = time.time() - start
    return QuestionResult(num_wrong, q_time, ("+", str(a), str(b)))


def subtraction(top: int) -> QuestionResult:
    num_wrong: int = 0
    a: int = random.randint(1, top)
    b: int = random.randint(1, top)
    start: float = time.time()
    ans: int = get_int(f"{a} - {b} = ")
    while ans != (a - b):
        num_wrong += wrong()
        ans = get_int(f"{a} - {b} = ")
    q_time: float = time.time() - start
    return QuestionResult(num_wrong, q_time, ("-", str(a), str(b)))


def plus_minus(top: int) -> QuestionResult:
    if random.random() < 0.5:  # noqa: PLR2004
        return addition(top)
    return subtraction(top)


def multiplication(top: int) -> QuestionResult:
    num_wrong: int = 0
    a: int = random.randint(1, top)
    b: int = random.randint(1, top)
    start: float = time.time()
    ans: int = get_int(f"{a} * {b} = ")
    while ans != (a * b):
        num_wrong += wrong()
        ans = get_int(f"{a} * {b} = ")
    q_time: float = time.time() - start
    return QuestionResult(num_wrong, q_time, ("*", str(a), str(b)))


def times_tables(top: int, num: int) -> QuestionResult:
    num_wrong: int = 0
    other_num: int = random.randint(1, top)
    if random.random() < 0.5:  # noqa: PLR2004
        a: int = num
        b: int = other_num
    else:
        a: int = other_num
        b: int = num
    start: float = time.time()
    ans: int = get_int(f"{a} * {b} = ", pos=True)
    while ans != (a * b):
        num_wrong += wrong()
        ans = get_int(f"{a} * {b} = ", pos=True)
    q_time: float = time.time() - start
    return QuestionResult(num_wrong, q_time, ("*", str(num), str(other_num)))


def powers(top: int, base: int) -> QuestionResult:
    num_wrong: int = 0
    exponent: int = random.randint(1, top)
    start: float = time.time()
    ans: int = get_int(f"{base}^{exponent} = ", pos=True)
    while ans != (base**exponent):
        num_wrong += wrong()
        ans = get_int(f"{base}^{exponent} = ", pos=True)
    q_time: float = time.time() - start
    return QuestionResult(num_wrong, q_time, ("^", str(base), str(exponent)))


# Defines what the maximum divisor will be.
# A value of 5 makes the largest possible divisor
# one-fifth of the dividend.
DIVISOR_MAX: int = 5


def division(top: int) -> QuestionResult:
    num_wrong: int = 0
    dividend: int = random.randint(1, top)
    divisor: int = random.randint(1, max(floor(dividend / DIVISOR_MAX), 1))
    print(f"{dividend} / {divisor} = ")
    start: float = time.time()
    quotient: int = get_int("Quotient = ")
    remainder: int = get_int("Remainder = ")
    while (quotient, remainder) != divmod(dividend, divisor):
        num_wrong += wrong()
        print(f"{dividend} / {divisor} = ")
        quotient = get_int("Quotient = ")
        remainder = get_int("Remainder = ")
    q_time: float = time.time() - start
    return QuestionResult(num_wrong, q_time, ("/", str(dividend), str(divisor)))


def square(top: int) -> QuestionResult:
    num_wrong: int = 0
    a: int = random.randint(1, top)
    start: float = time.time()
    ans: int = get_int(f"{a}^2 = ")
    while int(ans) != (a**2):
        num_wrong += wrong()
        ans = get_int(f"{a}^2 = ")
    q_time: float = time.time() - start
    return QuestionResult(num_wrong, q_time, ("^", str(a), "2"))


######################################################
# defines how close a guess has to be for squareroot()
# a value of 0.01 means that an answer has to be within 1%
# of the true root to be correct
TOLERANCE: float = 0.01


def squareroot(top: int) -> QuestionResult:
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
        num_wrong += wrong()
        ans = get_expr(f"sqrt({a}) = ")
    q_time: float = time.time() - start
    print()
    label = "Newton's method approximation:"
    print(f"{Fore.BLUE}{label:<30} {Fore.YELLOW}{best_answer}{Fore.RESET}")
    print(f"{Fore.BLUE}{'Range:':<30} {Fore.YELLOW}{correct_range}{Fore.RESET}")
    print(f"{Fore.BLUE}{'Actual:':<30} {Fore.YELLOW}{true_root}{Fore.RESET}")
    print(
        f"{Fore.BLUE}{'Difference:':<30} "
        f"{Fore.YELLOW}{abs(best_answer - true_root)}{Fore.RESET}"
    )
    q: str = (
        input(f"{Fore.GREEN}Press enter to continue...\n{Fore.RESET}").strip().lower()
    )
    quit_check(q)
    return QuestionResult(num_wrong, q_time, ("sqrt", str(a)))


def perfect_square(top: int) -> QuestionResult:
    num_wrong: int = 0
    top = floor(sqrt(top))
    a: int = random.randint(1, top)
    start: float = time.time()
    ans: float = get_int(f"sqrt({a**2}) = ")
    while ans != a:
        num_wrong += wrong()
        ans = get_expr(f"sqrt({a**2}) = ")
    q_time: float = time.time() - start
    return QuestionResult(num_wrong, q_time, ("sqrt", str(a**2)))


def print_complex_number(a: int, b: int) -> str:
    if b > 0:
        return f"{a} + {b}i"
    return f"{a} - {abs(b)}i"


def complex_multiplication(top: int) -> QuestionResult:
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
        num_wrong += wrong()
        print(f"({print_complex_number(a, b)}) * ({print_complex_number(c, d)}) = ")
        real_part_ans: int = get_int("Real = ")
        imaj_part_ans: int = get_int("Imaj = ")
    q_time: float = time.time() - start
    return QuestionResult(
        num_wrong,
        q_time,
        ("*", f"({print_complex_number(a, b)})", f"({print_complex_number(c, d)})"),
    )


def default() -> Callable[[], QuestionResult]:
    ops: list[tuple[Callable[[int], QuestionResult], int]] = [
        (addition, 999),
        (subtraction, 999),
        (multiplication, 99),
        (division, 999),
        (square, 99),
        (squareroot, 99),
    ]

    def inner() -> QuestionResult:
        func, limit = random.choice(ops)
        return func(limit)

    return inner


def random_date() -> datetime.date:
    start = datetime.date(1600, 1, 1)
    end = datetime.date(2099, 12, 31)
    return datetime.date.fromordinal(random.randint(start.toordinal(), end.toordinal()))


def calendar() -> QuestionResult:
    num_wrong: int = 0
    a = random_date()
    start: float = time.time()
    ans: int = get_day(f"The day of the week of {a.strftime('%B %d, %Y')} is ")
    while ans != ((a.weekday() + 1) % 7):
        num_wrong += wrong()
        ans = get_int(f"The day of the week of {a.strftime('%B %d, %Y')} is ")
    q_time: float = time.time() - start
    return QuestionResult(num_wrong, q_time, ("cal", a.strftime("%B %d, %Y")))
