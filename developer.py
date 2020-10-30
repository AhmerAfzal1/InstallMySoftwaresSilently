from colorama import init, Fore, Style
import constant as const
import functions as func
import main

android_studio = "Android Studio 4.1.0 (201.6858069)"
git = "Git 2.28.0"
java_jdk = "Java  JDK 8 Update 271"
notepad_p_p = "Notepad++ 7.8.9"
python = "Python 3.9.0"


def main_developer():
    func.set_console_title(const.heading_developer)
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

            choice = int(input("\nPlease enter your choice: "))

            if choice == 0:
                print("\nValue must be greater than zero")
                input()
                func.clear_screen()
                continue

            elif choice == 1:
                func.clear_screen()
                main.main()
                break

            elif choice == 7:
                exit()
                break

            else:
                print("\nThat is not between 1 To 6! Try Again\n")
                input()
                func.clear_screen()
                continue

        except ValueError:
            print("\nPlease input a number")
            input()
            func.clear_screen()


if __name__ == "__main__":
    init()
    main_developer()
