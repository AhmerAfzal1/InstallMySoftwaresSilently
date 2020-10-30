from colorama import init, Fore, Style
import constant as const
import developer
import functions as func
import internet


def main():
    while True:
        try:
            print(Fore.CYAN + const.heading_main_title + Style.RESET_ALL)
            print("\n")
            func.main_heading_softwares("01", "All Drivers & Recommended")
            func.main_heading_softwares("02", "Developer")
            func.main_heading_softwares("03", "Internet")
            func.main_heading_softwares("04", "Major")
            func.main_heading_softwares("05", "Mobile")
            func.main_heading_softwares("06", "Multimedia")
            func.main_heading_softwares("07", "PDF")
            func.main_heading_softwares("08", "Utilities")
            func.eixt_heading("09")

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
    func.set_console_title("Ahmer's Automaticalling And Silently Software Installation Program")
    main()
    # install_software(adobe_acrobat_reader, "Setup.exe")
