import sys
from getpass import getpass

import vk
from vk.exceptions import VkAuthError

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
    print('{:-<30}'.format(''))
    print('{:^30}'.format('Your VK Friends Online:'))
    print('{:-<30}'.format(''))

    if not friends_online:
        print('You have no friends online')
        return

    for friend in sorted(friends_online, key=lambda item: item['first_name']):
        print('{} {}'.format(friend['first_name'], friend['last_name']))


def main():
    login = input('Enter login: ')

    if not login:
        sys.exit('Login is empty')

    password = getpass(prompt='Enter password: ')

    try:
        friends_online = get_online_friends(login, password)
    except VkAuthError:
        sys.exit('Incorrect login or password')

    output_friends_to_console(friends_online)


if __name__ == '__main__':
    main()
