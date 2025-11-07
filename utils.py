import os
import shutil

import numexpr
from colorama import Fore


def quit_check(check: str) -> None:
    if check.lower().strip() == "q":
        os.system("clear")
        raise SystemExit


def get_maxes(operation: str) -> int | None:
    while True:
        user_input = (
            input(
                Fore.BLUE
                + "Enter a maximum for "
                + Fore.YELLOW
                + f"{operation.strip().lower()}"
                + Fore.BLUE
                + ", or "
                + Fore.YELLOW
                + "[Enter]"
                + Fore.BLUE
                + " to skip: "
                + Fore.RESET
            )
            .lower()
            .strip()
        )
        quit_check(user_input)
        if user_input == "":
            print(Fore.GREEN + "Skipping..." + Fore.RESET)
            return None
        try:
            num: int = int(user_input)
            if num < 1:
                print(
                    Fore.RED
                    + "Invalid input. Please enter an integer greater than 0."
                    + Fore.RESET
                )
                continue
            break
        except ValueError:
            print(
                Fore.RED
                + "Invalid input. Please enter an integer greater than 0."
                + Fore.RESET
            )
    return num


def get_float(message: str) -> float:
    while True:
        user_input = input(message).lower().strip()
        quit_check(user_input)
        try:
            num: float = float(user_input)
            break
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid number." + Fore.RESET)
    return num


def get_int(message: str, pos: bool = False) -> int:
    while True:
        user_input = input(message).lower().strip()
        quit_check(user_input)
        try:
            num: int = int(user_input)
            if (num < 1) and pos:
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
        quit_check(user_input)
        try:
            num = numexpr.evaluate(user_input)
            num = float(num)
            break
        except Exception:
            print(
                Fore.RED
                + "Invalid input. Please enter a valid expression."
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
