import time

from colorama import Fore

from config import (
    ALL_OPERATIONS,
    ROUNDING_NUM,
    configure,
    configure_custom,
    configure_times_tables,
    print_summary,
)
from utils import (
    RestartProgram,
    get_int,
    print_ui,
    quit_check,
)


def play_round(trial, num_q: int, *args: int):
    errors: int = 0
    q_times: list[float] = []
    question_log: dict[tuple[str, int, int] | tuple[str, int], float] = {}
    start_round: float = time.time()
    for i in range(num_q):
        print_ui()
        print(Fore.BLUE + f"Question {i + 1}\n" + Fore.RESET)
        n_errors, q_time, nums = trial(*args)
        errors += n_errors
        q_times.append(q_time)
        if nums in question_log:
            question_log[nums] = (question_log[nums] + q_time) / 2
        else:
            question_log[nums] = q_time
        print_ui()
    end_round: float = time.time()
    print_ui()
    print_summary(num_q, errors, start_round, end_round, q_times)
    return question_log


LIMIT: int = 10


def print_data(q_log: dict[tuple[str, int, int] | tuple[str, int], float]) -> None:
    message: str = f"\n{Fore.BLUE}Averages:"
    sorted_questions = sorted(q_log.items(), key=lambda item: item[1], reverse=True)
    print(message)
    number_data = [item[0] for item in sorted_questions]
    q_times = [item[1] for item in sorted_questions]
    try:
        l_width: int = 0
        r_width: int = 0
        q_width: int = 0
        for _, a, b in number_data:
            l_width = max(l_width, len(str(a)))
            r_width = max(r_width, len(str(b)))
        for q_time in q_times:
            num = round(q_time, ROUNDING_NUM)
            q_width = max(q_width, len(str(num)))
        for op_nums, q_time in sorted_questions:
            op, *nums = op_nums
            a, b = nums
            print(
                Fore.BLUE
                + f"{a:>{l_width}}"
                + Fore.YELLOW
                + f" {op} "
                + Fore.BLUE
                + f"{b:<{r_width}}"
                + Fore.GREEN
                + f" | {round(q_time, ROUNDING_NUM):<{q_width}} seconds"
                + Fore.RESET
            )
    except ValueError:
        width: int = 0
        q_width: int = 0
        for _, a in number_data:
            width = max(width, len(str(a)))
        for q_time in q_times:
            num = round(q_time, ROUNDING_NUM)
            q_width = max(q_width, len(str(num)))
        for op_nums, q_time in sorted_questions:
            op, *nums = op_nums
            a = nums[0]
            print(
                Fore.BLUE
                + f"{a:>{width}}"
                + Fore.YELLOW
                + f" {op} "
                + Fore.GREEN
                + "| "
                + f"{round(q_time, ROUNDING_NUM):<{q_width}} seconds"
                + Fore.RESET
            )


def again_msg() -> None:
    print(
        "\n"
        + Fore.BLUE
        + "Again? ("
        + Fore.GREEN
        + "y"
        + Fore.BLUE
        + "/"
        + Fore.RED
        + "n"
        + Fore.BLUE
        + f"), or {Fore.YELLOW}d{Fore.BLUE} to view data."
        + Fore.RESET
    )


def main_loop(*args) -> None:
    again: str = "y"
    while True:
        question_log = play_round(*args)
        while True:
            again_msg()
            again = input().lower().strip()
            quit_check(again)
            if again == "y":
                break
            if again == "n":
                return
            if again == "d":
                print_data(question_log)
            else:
                print(Fore.RED + "Invalid input." + Fore.RESET)


# Special cases for the default and custom function
# as those have different ways of defining max number


def main() -> None:
    try:
        while True:
            print_ui()
            op, num_q = configure()
            if op == "custom":
                trial = configure_custom()
                main_loop(trial, num_q)
                continue
            if op == "default":
                trial = ALL_OPERATIONS[op]
                main_loop(trial, num_q)
                continue
            if op in {"times tables", "tt"}:
                trial = configure_times_tables()
            else:
                trial = ALL_OPERATIONS[op]
            print(Fore.BLUE + "What is the max number?" + Fore.RESET)
            top = get_int(Fore.GREEN + "Enter a number: " + Fore.RESET, pos=True)
            main_loop(trial, num_q, top)
    except RestartProgram:
        main()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + Fore.BLUE + "Program interrupted. Exiting..." + Fore.RESET)
