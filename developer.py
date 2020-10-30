from colorama import init, Fore, Style
import functions as func

android_studio = "Android Studio 4.1.0 (201.6858069)"
git = "Git 2.28.0"
java_jdk = "Java  JDK 8 Update 271"
notepad_p_p = "Notepad++ 7.8.9"
python = "Python 3.9.0"


def main_developer():
    init()
    while True:
        try:
            print(Fore.CYAN + "Ahmer's Automaticalling And Silently Software Installation Program" + Style.RESET_ALL)
            print("\n")
            print(Fore.CYAN + "Developer Softwares" + Style.RESET_ALL)
            print("\n")
            func.my_coloured_str("01", android_studio)
            func.my_coloured_str("02", java_jdk)
            func.my_coloured_str("03", python)
            func.my_coloured_str("04", git)
            func.my_coloured_str("05", notepad_p_p)
            print(Fore.RED + "[06] Eixt".upper() + Style.RESET_ALL)

            choice = int(input("\nPlease enter your choice: "))

            if choice == 0:
                print("\nValue must be greater than zero")
                input()
                func.clear_screen()
                continue

            elif choice == 1:
                print("Please wait")
                break

            elif choice == 6:
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
    main_developer()
