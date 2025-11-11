import random
import statistics

from colorama import Fore

from operations import (
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
        print(Fore.YELLOW + f" {op:>{width}}" + Fore.BLUE + f" | {desc}" + Fore.RESET)
    print("\n")


def configure() -> tuple[str, int]:
    operations = ALL_OPERATIONS.keys()
    while True:
        print(
            Fore.BLUE + f"What do you want to practice? "
            f"Enter {Fore.YELLOW}l{Fore.BLUE} for options." + Fore.RESET
        )
        op: str = input(Fore.GREEN + "Operation: " + Fore.RESET).lower().strip()
        quit_check(op)
        if op == "l":
            print_options()
            continue
        if op in operations:
            break
        print(Fore.RED + "Invalid input." + Fore.RESET)
    print(Fore.BLUE + "How many questions?" + Fore.RESET)
    num_q: int = get_int(Fore.GREEN + "Enter a number: " + Fore.RESET, pos=True)
    return op, num_q


# These are the options that are included in the 'custom' setting
CUSTOM_OPERATIONS = {
    "addition": addition,
    "subtraction": subtraction,
    "multiplication": multiplication,
    "complex multiplication": complex_multiplication,
    "division": division,
    "square": square,
    "square root": squareroot,
}


def configure_custom():
    while True:
        user_opts: dict[str, int | None] = {}
        for operation in CUSTOM_OPERATIONS:
            top = get_maxes(operation)
            if top:
                user_opts[operation] = top
        if not user_opts:
            print(Fore.RED + "Error: please specify at least one maximum." + Fore.RESET)
            continue
        break

    def custom() -> int:
        question = random.choice(list(user_opts.keys()))
        return CUSTOM_OPERATIONS.get(question)(user_opts[question])

    return custom


def configure_times_tables():
    print(Fore.BLUE + "Which times table do you want to practice?" + Fore.RESET)
    table_number: int = get_int(Fore.GREEN + "Enter a number: " + Fore.RESET, pos=True)

    def inner(top: int) -> tuple[int, float, tuple[str, int, int]]:
        return times_tables(top, table_number)

    return inner


def configure_powers():
    print(Fore.BLUE + "Which base number do you want to practice?" + Fore.RESET)
    base: int = get_int(Fore.GREEN + "Enter a number: " + Fore.RESET, pos=True)

    def inner(top: int) -> tuple[int, float, tuple[str, int, int]]:
        return powers(top, base)

    return inner


def print_summary(
    num_q: int, errors: int, start_round: float, end_round: float, q_times: list[float]
) -> None:
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
        + f" {'error' if errors == 1 else 'errors'}.\n"
        + Fore.RESET
    )
    width: int = 20
    print(
        Fore.BLUE
        + f"{'Average time:':<{width}}"
        + Fore.YELLOW
        + f"{round(statistics.mean(q_times), ROUNDING_NUM)}"
        + Fore.BLUE
        + " seconds"
        + Fore.RESET
    )
    if len(q_times) > 1:
        print(
            Fore.BLUE
            + f"{'Standard deviation:':<{width}}"
            + Fore.YELLOW
            + f"{round(statistics.stdev(q_times), ROUNDING_NUM):<4}"
            + Fore.BLUE
            + " seconds"
            + Fore.RESET
        )
        print(
            Fore.BLUE
            + f"{'Median time:':<{width}}"
            + Fore.YELLOW
            + f"{round(statistics.median(q_times), ROUNDING_NUM):<4}"
            + Fore.BLUE
            + " seconds"
            + Fore.RESET
        )
        print(
            Fore.BLUE
            + f"{'Shortest time:':<{width}}"
            + Fore.YELLOW
            + f"{round(min(q_times), ROUNDING_NUM):<4}"
            + Fore.BLUE
            + " seconds"
            + Fore.RESET
        )
        print(
            Fore.BLUE
            + f"{'Longest time:':<{width}}"
            + Fore.YELLOW
            + f"{round(max(q_times), ROUNDING_NUM):<4}"
            + Fore.BLUE
            + " seconds"
            + Fore.RESET
        )
        print(
            Fore.BLUE
            + f"{'Range:':<{width}}"
            + Fore.YELLOW
            + f"{round(max(q_times) - min(q_times), ROUNDING_NUM):<4}"
            + Fore.BLUE
            + " seconds\n"
            + Fore.RESET
        )


ALL_OPERATIONS = {
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
