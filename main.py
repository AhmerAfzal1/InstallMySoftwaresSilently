from colorama import init
import constant as const
import ctypes
import developer
import enum
import functions as func
import internet
import os
import sys


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


def make_font_bigger():
    lf_facesize = 32
    std_output_handle = -11

    class Coord(ctypes.Structure):
        _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

    class ConsoleFontInfoex(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_ulong),
                    ("nFont", ctypes.c_ulong),
                    ("dwFontSize", Coord),
                    ("FontFamily", ctypes.c_uint),
                    ("FontWeight", ctypes.c_uint),
                    ("FaceName", ctypes.c_wchar * lf_facesize)]

    font = ConsoleFontInfoex()
    font.cbSize = ctypes.sizeof(ConsoleFontInfoex)
    font.nFont = 12
    font.dwFontSize.X = 11
    font.dwFontSize.Y = 16  # Font size value
    font.FontFamily = 54
    font.FontWeight = 400
    font.FaceName = "Lucida Console"

    handle = ctypes.windll.kernel32.GetStdHandle(std_output_handle)
    ctypes.windll.kernel32.SetCurrentConsoleFontEx(handle, ctypes.c_long(False), ctypes.pointer(font))


def main():
    make_font_bigger()
    os.system("mode 110, 33")
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
                    developer.main_program()
                    break

                elif choice == 3:
                    func.clear_screen()
                    internet.main_program()
                    break

                elif choice == 4 or choice == 5 or choice == 6 or choice == 7 or choice == 8:
                    func.under_progress_heading("This feature is under progress")
                    input()
                    func.clear_screen()
                    continue

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
