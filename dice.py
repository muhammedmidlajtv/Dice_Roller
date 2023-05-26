import random


def rolldice():
    num = random.randint(1, 6)
    return num


def main():
    print("\t\t\t😃😃😃😃😃 WELCOME 😃😃😃😃😃\t\t\t")
    while 1:
        option = input("❁ Enter 'R' to  roll your dice and 'E' for exit:\n🎯➡")
        if option == 'R':
            print('Number on  your dice : ', end='')
            print(rolldice())
        elif option == 'E':
            break
        else:
            print("Invalid option 😕")

    print("Thank you for playing , Have a nice day 🌞")

main()
