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


class QuestionLog:
    def __init__(self):
        self.log = {}

    def update(self, question, q_time: float, num_errors: int) -> None:
        if question in self.log:
            new_time = (self.log[question]["time"] + q_time) / 2
            new_errors = self.log[question]["n_errors"] + num_errors
            self.log[question] = {"time": new_time, "n_errors": new_errors}
        else:
            self.log[question] = {"time": q_time, "n_errors": num_errors}

    def print_data(self) -> None:
        sorted_questions = sorted(
            self.log.items(), key=lambda item: item[1]["time"], reverse=True
        )
        number_data = [item[0] for item in sorted_questions]
        q_times = [item[1]["time"] for item in sorted_questions]
        l_width: int = 0
        r_width: int = 0
        q_width: int = 0
        op_width: int = 0
        for data in number_data:
            op_width = max(op_width, len(data[0]))
            l_width = max(l_width, len(str(data[1])))
            if len(data) == 3:
                r_width = max(r_width, len(str(data[2])))
        for q_time in q_times:
            num = round(q_time, ROUNDING_NUM)
            q_width = max(q_width, len(str(num)))
        for op_nums, result_dict in sorted_questions:
            op, *nums = op_nums
            a = nums[0]
            b = nums[1] if len(nums) == 2 else ""
            print(
                Fore.BLUE
                + f"{a:>{l_width}}"
                + Fore.YELLOW
                + f" {op:^{op_width}} "
                + Fore.BLUE
                + f"{b:<{r_width}}"
                + Fore.GREEN
                + f" | {round(result_dict['time'], ROUNDING_NUM):<{q_width}} seconds"
                + " | "
                + Fore.RESET,
                end="",
            )
            if result_dict["n_errors"] != 0:
                print(
                    Fore.RED + f"{result_dict['n_errors']} error" + Fore.RESET,
                    end="",
                )
                if result_dict["n_errors"] > 1:
                    print(Fore.RED + "s" + Fore.RESET, end="")
            print()


def play_round(trial, num_q: int, *args: int) -> QuestionLog:
    total_errors: int = 0
    q_times: list[float] = []
    question_log = QuestionLog()
    start_round: float = time.time()
    for i in range(num_q):
        print_ui()
        print(Fore.BLUE + f"Question {i + 1}\n" + Fore.RESET)
        n_errors, q_time, nums = trial(*args)
        total_errors += n_errors
        q_times.append(q_time)
        question_log.update(nums, q_time, n_errors)
    end_round: float = time.time()
    print_ui()
    print_summary(num_q, total_errors, start_round, end_round, q_times)
    return question_log


def print_data(q_log: QuestionLog) -> None:
    print()
    q_log.print_data()


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
