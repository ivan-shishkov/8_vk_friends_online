import sys
from getpass import getpass

import vk

APP_ID = -1  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    # например, api.friends.get()


def output_friends_to_console(friends_online):
    pass


def main():
    login = input('Enter login: ')

    if not login:
        sys.exit('Login is empty')

    password = getpass(prompt='Enter password: ')

    if not password:
        sys.exit('Password is empty')

    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)


if __name__ == '__main__':
    main()
