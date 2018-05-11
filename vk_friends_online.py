import sys
from getpass import getpass

import vk

APP_ID = 6475461


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    api = vk.API(session, v='5.74')

    friends_online_ids = api.friends.getOnline()

    return api.users.get(user_ids=friends_online_ids)


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
