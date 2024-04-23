import os


def clear_console():
    # Clear console command for Windows, Linux, and MacOS
    os.system("cls" if os.name == "nt" else "clear")
