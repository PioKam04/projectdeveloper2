from models.data import clients
from utils.crud import show_client, add_client, remove_client, update_client

def main() -> None:
    while True:
        print("Welcome to the menu  ")
        print("0. Exit ")
        print("1. Read a list of friends ")
        print("2. Add new user")
        print("3. Search user")
        print("4. Remove user")
        print("5. Update user")
        print("6. Generate single map")
        print("7. Generate full map")

        menu_option = input("Choose an option:")
        if menu_option == "0": break
        if menu_option == "1": show_client(clients)
        if menu_option == "2": add_client(clients)
        if menu_option == "4": remove_client(clients)
        if menu_option == "5": update_client(clients)


if __name__ == '__main__':
    main()