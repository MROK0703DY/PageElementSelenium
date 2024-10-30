import sys
import time
import datetime
from datetime import datetime as dt
from print_жирный_и_цветной_текст import Color


number = "30 октября"
time_hour = "21"
day = "СРД"


def p(*args) -> None:
    """Функция печати.Строка с пунктуацией.Печатает в консоль."""
    print(*args)


def sys_executable() -> None:
    """Вывод на печать пути к инерпретатору."""
    print()
    print(f"Путь к инерпретатору: {sys.executable}")
    print()


def get_date_one() -> None:
    """Вывод на печать текущей даты и времени."""
    x = datetime.date.isoformat(datetime.date.today())
    y = f"{x[8:]} октября {x[:4]}"
    z = time.strftime("%H:%M:%S")
    p(f"{Color.BOLD}, {Color.PURPLE}{x}\n{y} {z}{Color.END}")
    p()


def get_date_two(number, time_hour, day) -> None:
    """Вывод на печать текущей даты и времени."""
    current_time = time.time()
    local_time = time.localtime(current_time)

    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S", local_time)
    print(formatted_time)
    p()
    ft = formatted_time.split()
    p(f"{Color.BOLD}{Color.GREEN} {ft[0]} {time_hour}{ft[1][2:]} {day}{Color.END}")
    p()


def get_date_three() -> None:
    """Вывод на печать текущей даты и времени."""
    d, ct = (str(dt.now()).split())
    d = d.split("-")
    d[1] = "октября"
    d = (list(reversed(d)))
    d = ' '.join(d)
    ct = ct.split(".")[0]
    t = ct.split(":")
    t[0] = str(int(t[0]))
    t = ':'.join(t)
    a_time = dt.now().strftime('%a')
    p(f"{Color.BOLD}{Color.BLUE}{d} {t} {a_time}{Color.END}")
    p()


def short_entry() -> None:
    """Вывод на печать текущей даты и времени."""
    a_time = dt.now().strftime('%a')
    current_time = str(dt.now()).split()[1].split(("."))[0]
    date = " ".join(["октября" if x == "10" else x for x in ((str(dt.now()).split())[0].split("-")[::-1])]) + " " + a_time
    p(f"{Color.BOLD}{Color.RED}{date} {current_time}{Color.END}")
    p()


def main() -> None:
    """Главная функция.Точка входа в программу."""
    sys_executable()
    get_date_one()
    get_date_two(number, time_hour, day)
    get_date_three()
    short_entry()


if __name__ == "__main__":
    main()
