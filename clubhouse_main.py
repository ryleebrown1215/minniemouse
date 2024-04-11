from encode import Encoder
from decode import Decode

def display_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    option = int(input("\nPlease enter an option: "))
    return option

def main():
    option = display_menu()
    while True:
        if option == 1:
            password = input("Please enter your password to encode: ")
            p = Encoder(password)
            encoded_password = p.encode()
            print("Your password has been encoded!")
            option = display_menu()
        elif option == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {p.password}.")
            option = display_menu()
        elif option == 3:
            break

if __name__ == "__main__":
    main()
