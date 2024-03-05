import os
import sys
from os.path import join, exists
from pathlib import Path


PASSWORD_DIR = "password"
ERR_MSG = "Incorrect username or password"


def cocaine(string: str, length: int = 128) -> str:
    res = 0
    for char in string:
        res += ord(char) ** ord(char) ** (res % 3)
    return ''.join(reversed(str(res)))[:length]


def create_user(username: str, password: str) -> None:
    password_path = Path(join(PASSWORD_DIR, username))
    password_path.parent.mkdir(parents=True, exist_ok=True)
    with open(password_path, 'w+') as password_file:
        password_file.write(cocaine(username + password))


def check_password(username: str, password: str) -> bool:
    try:
        with open(join(PASSWORD_DIR, username)) as password_file:
            return cocaine(username + password) == password_file.read().strip()

    except FileNotFoundError:
        pass
    return False


def delete_user(username: str):
    try:
        os.remove(join(PASSWORD_DIR, username))
    except FileNotFoundError:
        return False
    return True


def main() -> None:

    while True:
        usr_input = input("1 for new user\n2 for login\n3 for delete user\n")

        username = input("Username: ")
        password = input("Password: ")

        if usr_input == '1':
            create_user(username, password)
            print("User created!")
            continue
        elif usr_input == '2':
            if check_password(username, password):
                print('Congratulations, you win! :)')
                continue

        elif usr_input == '3':
            if check_password(username, password):
                if delete_user(username):
                    print(f'User "{username}" successfully deleted!')
                    continue

        print(ERR_MSG)


if __name__ == '__main__':
    main()
