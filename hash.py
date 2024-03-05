import sys
from os.path import join, exists
from pathlib import Path


PASSWORD_DIR = "password"
ERR_MSG = "Incorrect username or password"


def cocaine(string: str) -> str:
    res = 0
    for char in string:
        res += ord(char) ** ord(char) ** (res % 3)
    return ''.join(reversed(str(res)))[:128]


def main() -> None:

    while True:
        usr_input = input("1 for new user\n2 for login")

        username = input("Username: ")
        password = input("Password: ")

        if usr_input == '1':
            password_path = Path(join(PASSWORD_DIR, username + '.txt'))
            password_path.parent.mkdir(parents=True, exist_ok=True)
            with open(password_path, 'w+') as password_file:
                password_file.write(cocaine(username + password))
            print("User created!")
        elif usr_input == '2':

            try:
                with open(join(PASSWORD_DIR, username + '.txt')) as password_file:
                    if cocaine(username + password) == password_file.read().strip():
                        print('Congratulations, you win! :)')
                        continue

            except FileNotFoundError:
                pass

            print(ERR_MSG)
            continue


if __name__ == '__main__':
    main()
