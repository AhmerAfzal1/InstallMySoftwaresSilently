from colorama import init, Fore, Style
import developer
import functions as func


def main():
    while True:
        try:
            print(Fore.CYAN + "Ahmer's Automaticalling And Silently Software Installation Program" + Style.RESET_ALL)
            print("\n")
            func.my_coloured_str("01", "All Drivers & Recommended")
            func.my_coloured_str("02", "Developer")
            func.my_coloured_str("03", "Internet")
            func.my_coloured_str("04", "Major")
            func.my_coloured_str("05", "Mobile")
            func.my_coloured_str("06", "Multimedia")
            func.my_coloured_str("07", "PDF")
            func.my_coloured_str("08", "Utilities")
            print(Fore.RED + "[09] Eixt".upper() + Style.RESET_ALL)

            choice = int(input("\nPlease enter your choice: "))

            if choice == 0:
                print("\nValue must be greater than zero")
                input()
                func.clear_screen()
                continue

            elif choice == 1:
                print("Please wait")
                break

            elif choice == 2:
                developer.main_developer()
                func.clear_screen()
                break

            elif choice == 9:
                exit()
                break

            else:
                print("\nThat is not between 1 To 9! Try Again\n")
                input()
                func.clear_screen()
                continue

        except ValueError:
            print("\nPlease input a number")
            input()
            func.clear_screen()


if __name__ == "__main__":
    init()
    main()
    # install_software(adobe_acrobat_reader, "Setup.exe")
