import random
import statistics
from collections.abc import Callable

from colorama import Fore

from operations import (
    QuestionResult,
    addition,
    calendar,
    complex_multiplication,
    default,
    division,
    multiplication,
    perfect_square,
    plus_minus,
    powers,
    square,
    squareroot,
    subtraction,
    times_tables,
)
from utils import get_int, get_maxes, quit_check

ROUNDING_NUM: int = 2


# Used to list options, be sure to see ALL_OPERATIONS at the bottom of this file
ALL_OPTIONS = {
    "+": "addition",
    "-": "subtraction",
    "+/-": "addition and subtraction",
    "pm": "addition and subtraction",
    "+-": "addition and subtraction",
    "*": "multiplication",
    "complex": "complex multiplication",
    "/": "division with remainder",
    "^2": "square",
    "sq": "square",
    "pow": "powers of a specified base",
    "sqrt": "square root",
    "psq": "square roots of perfect squares",
    "times tables": "times tables",
    "tt": "alias for times tables",
    "cal": "find day of the week",
    "custom": "configure custom session",
    "default": "3 digit addition/subtraction, 2 digit multiplication, "
    "3 digit division, 2 digit squaring/square root",
}


def print_options() -> None:
    width: int = max(len(v) for v in ALL_OPTIONS)
    for op, desc in ALL_OPTIONS.items():
        print(f"{Fore.YELLOW} {op:>{width}}" + f"{Fore.BLUE} | {desc}{Fore.RESET}")
    print("\n")


def configure() -> tuple[str, int]:
    operations = ALL_OPERATIONS.keys()
    while True:
        print(
            f"{Fore.BLUE}What do you want to practice? "
            f"Enter {Fore.YELLOW}l{Fore.BLUE} for options.{Fore.RESET}"
        )
        op: str = input(f"{Fore.GREEN}Operation: {Fore.RESET}").lower().strip()
        quit_check(op)
        if op == "l":
            print_options()
            continue
        if op in operations:
            break
        print(f"{Fore.RED} Invalid input.{Fore.RESET}")
    print(f"{Fore.BLUE}How many questions?{Fore.RESET}")
    num_q: int = get_int(f"{Fore.GREEN}Enter a number: {Fore.RESET}", pos=True)
    return op, num_q


# These are the options that are included in the 'custom' setting
CUSTOM_OPERATIONS: dict[str, Callable[[int], QuestionResult]] = {
    "addition": addition,
    "subtraction": subtraction,
    "multiplication": multiplication,
    "complex multiplication": complex_multiplication,
    "division": division,
    "square": square,
    "square root": squareroot,
}


def configure_custom() -> Callable[[], QuestionResult]:
    while True:
        user_opts: dict[str, int] = {}
        for operation in CUSTOM_OPERATIONS:
            top = get_maxes(operation)
            if top:
                user_opts[operation] = top
        if not user_opts:
            print(f"{Fore.RED}Error: please specify at least one maximum.{Fore.RESET}")
            continue
        break

    def custom() -> QuestionResult:
        question = random.choice(list(user_opts.keys()))
        return CUSTOM_OPERATIONS[question](user_opts[question])

    return custom


def configure_times_tables() -> Callable[[int], QuestionResult]:
    print(f"{Fore.BLUE}Which times table do you want to practice?{Fore.RESET}")
    table_number: int = get_int(f"{Fore.GREEN}Enter a number: {Fore.RESET}", pos=True)

    def inner(top: int) -> QuestionResult:
        return times_tables(top, table_number)

    return inner


def configure_powers() -> Callable[[int], QuestionResult]:
    print(f"{Fore.BLUE}Which base number do you want to practice?{Fore.RESET}")
    base: int = get_int(f"{Fore.GREEN}Enter a number: {Fore.RESET}", pos=True)

    def inner(top: int) -> QuestionResult:
        return powers(top, base)

    return inner


def print_summary(
    num_q: int, errors: int, start_round: float, end_round: float, q_times: list[float]
) -> None:
    print(
        f"{Fore.BLUE}Solved "
        f"{Fore.YELLOW}{num_q}"
        f"{Fore.BLUE} problems in "
        f"{Fore.YELLOW}{round(end_round - start_round, ROUNDING_NUM)}"
        f"{Fore.BLUE} seconds with "
        f"{Fore.YELLOW}{errors}"
        f"{Fore.BLUE} {'error' if errors == 1 else 'errors'}.\n{Fore.RESET}"
    )
    width: int = 20
    print(
        f"{Fore.BLUE}{'Average time:':<{width}}"
        f"{Fore.YELLOW}{round(statistics.mean(q_times), ROUNDING_NUM)}"
        f"{Fore.BLUE} seconds{Fore.RESET}"
    )
    if len(q_times) > 1:
        print(
            f"{Fore.BLUE}{'Standard deviation:':<{width}}"
            f"{Fore.YELLOW}{round(statistics.stdev(q_times), ROUNDING_NUM):<4}"
            f"{Fore.BLUE} seconds{Fore.RESET}"
        )
        print(
            f"{Fore.BLUE}{'Median time:':<{width}}"
            f"{Fore.YELLOW}{round(statistics.median(q_times), ROUNDING_NUM):<4}"
            f"{Fore.BLUE} seconds{Fore.RESET}"
        )
        print(
            f"{Fore.BLUE}{'Shortest time:':<{width}}"
            f"{Fore.YELLOW}{round(min(q_times), ROUNDING_NUM):<4}"
            f"{Fore.BLUE} seconds{Fore.RESET}"
        )
        print(
            f"{Fore.BLUE}{'Longest time:':<{width}}"
            f"{Fore.YELLOW}{round(max(q_times), ROUNDING_NUM):<4}"
            f"{Fore.BLUE} seconds{Fore.RESET}"
        )
        print(
            f"{Fore.BLUE}{'Range:':<{width}}"
            f"{Fore.YELLOW}{round(max(q_times) - min(q_times), ROUNDING_NUM):<4}"
            f"{Fore.BLUE} seconds\n{Fore.RESET}"
        )


ALL_OPERATIONS: dict[str, Callable[..., QuestionResult]] = {
    "+": addition,
    "-": subtraction,
    "+/-": plus_minus,
    "pm": plus_minus,
    "+-": plus_minus,
    "*": multiplication,
    "complex": complex_multiplication,
    "/": division,
    "^2": square,
    "sq": square,
    "pow": powers,
    "sqrt": squareroot,
    "psq": perfect_square,
    "times tables": times_tables,
    "tt": times_tables,
    "cal": calendar,
    "custom": configure_custom,
    "default": default(),
}
