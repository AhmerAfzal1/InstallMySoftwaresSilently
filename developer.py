from colorama import init
import constant as const
import functions as func
import main

android_studio = "Android Studio 4.1.0 (201.6858069)"
git = "Git 2.28.0"
java_jdk = "Java  JDK 8 Update 271"
notepad_p_p = "Notepad++ 7.9.1"
python = "Python 3.9.0"


def main_developer():
    func.set_console_title(const.heading_developer)
    init()
    while True:
        try:
            func.main_heading()
            func.sub_heading(const.heading_developer)
            func.back_heading()
            func.sub_heading_softwares("02", android_studio)
            func.sub_heading_softwares("03", java_jdk)
            func.sub_heading_softwares("04", python)
            func.sub_heading_softwares("05", git)
            func.sub_heading_softwares("06", notepad_p_p)
            func.eixt_heading("07")

            choice = func.input_heading()

            if choice == 0:
                func.exception_heading("Value must be greater than zero")
                input()
                func.clear_screen()
                continue

            elif choice == 1:
                func.clear_screen()
                main.main()
                break

            elif choice == 2:
                func.install_software(android_studio, "Setup.exe /S /Allusers")
                func.clear_screen()
                continue

            elif choice == 6:
                func.install_software(notepad_p_p, "Setup.exe /S")
                func.clear_screen()
                continue

            elif choice == 7:
                exit()
                break

            else:
                func.exception_range_heading("1", "7")
                input()
                func.clear_screen()
                continue

        except ValueError:
            func.exception_heading("Please input a number")
            input()
            func.clear_screen()
