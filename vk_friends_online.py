import sys
from getpass import getpass

import vk
from vk.exceptions import VkAuthError


def get_friends_online_info(
        application_id,
        user_login,
        user_password,
        api_version='5.74'):
    session = vk.AuthSession(
        app_id=application_id,
        user_login=user_login,
        user_password=user_password,
        scope='friends',
    )
    api = vk.API(session, v=api_version)

    friends_online_ids = api.friends.getOnline()

    return api.users.get(user_ids=friends_online_ids)


def print_friends_online(friends_online):
    print('{:-<30}'.format(''))
    print('{:^30}'.format('Your VK Friends Online:'))
    print('{:-<30}'.format(''))

    if not friends_online:
        print('You have no friends online')
        return

    for friend in sorted(friends_online, key=lambda item: item['first_name']):
        print('{} {}'.format(friend['first_name'], friend['last_name']))


def main():
    print('Enter your VK credentials:')

    user_login = input('Enter login: ')

    if not user_login:
        sys.exit('Login is empty')

    user_password = getpass(prompt='Enter password: ')

    if not user_password:
        sys.exit('Password is empty')

    try:
        friends_online = get_friends_online_info(
            application_id=6475461,
            user_login=user_login,
            user_password=user_password,
        )
    except VkAuthError:
        sys.exit('Incorrect login or password')

    print_friends_online(friends_online)


if __name__ == '__main__':
    main()
