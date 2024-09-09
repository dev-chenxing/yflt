import threading
from rich import print

from core import timer
from help.welcome import welcome
# from cmds import time

print(welcome)

timer.game_time = timer.Time()
timer.real_time = timer.Time()

try:

    running = True

    game_time_thread = threading.Thread(
        target=timer.game_time_thread, daemon=True)
    real_time_thread = threading.Thread(
        target=timer.real_time_thread, daemon=True)

    game_time_thread.start()
    real_time_thread.start()

    while running:
        cmd = input("> ")
        if cmd == "time":
            print(f"现在 游戏 时间是：[bright_yellow]{
                timer.game_time.format()}[/bright_yellow]")

except (KeyboardInterrupt, SystemExit):
    print(":x: 退出")
