from colorama import init
import constant as const
import developer
import enum
import functions as func
import internet
import os
import sys
import ctypes


class SW(enum.IntEnum):
    HIDE = 0
    MAXIMIZE = 3
    MINIMIZE = 6
    RESTORE = 9
    SHOW = 5
    SHOWDEFAULT = 10
    SHOWMAXIMIZED = 3
    SHOWMINIMIZED = 2
    SHOWMINNOACTIVE = 7
    SHOWNA = 8
    SHOWNOACTIVATE = 4
    SHOWNORMAL = 1


class ERROR(enum.IntEnum):
    ZERO = 0
    FILE_NOT_FOUND = 2
    PATH_NOT_FOUND = 3
    BAD_FORMAT = 11
    ACCESS_DENIED = 5
    ASSOC_INCOMPLETE = 27
    DDE_BUSY = 30
    DDE_FAIL = 29
    DDE_TIMEOUT = 28
    DLL_NOT_FOUND = 32
    NO_ASSOC = 31
    OOM = 8
    SHARE = 26


def main():
    os.system("mode 120, 35")
    func.set_console_title(const.heading_main_title)
    init()
    if ctypes.windll.shell32.IsUserAnAdmin():
        while True:
            try:
                func.main_heading()
                func.main_heading_softwares("01", "All Drivers & Recommended")
                func.main_heading_softwares("02", "Developer")
                func.main_heading_softwares("03", "Internet")
                func.main_heading_softwares("04", "Major")
                func.main_heading_softwares("05", "Mobile")
                func.main_heading_softwares("06", "Multimedia")
                func.main_heading_softwares("07", "PDF")
                func.main_heading_softwares("08", "Utilities")
                func.eixt_heading("09")

                choice = func.input_heading()

                if choice == 0:
                    func.exception_heading("Value must be greater than zero")
                    input()
                    func.clear_screen()
                    continue

                elif choice == 1:
                    print("Please wait")
                    break

                elif choice == 2:
                    func.clear_screen()
                    developer.main_developer()
                    break

                elif choice == 3:
                    func.clear_screen()
                    internet.main_developer()
                    break

                elif choice == 9:
                    exit()
                    break

                else:
                    func.exception_range_heading("1", "9")
                    input()
                    func.clear_screen()
                    continue

            except ValueError:
                func.exception_heading("Please input a number")
                input()
                func.clear_screen()
    else:
        hinstance = ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, sys.argv[0], None, SW.SHOWNORMAL)
        if hinstance <= 32:
            raise RuntimeError(ERROR(hinstance))


if __name__ == "__main__":
    main()
    # install_software(adobe_acrobat_reader, "Setup.exe")
