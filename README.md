# Watcher of Friends Online

This script allows to watch for your friends in social network Vkontakte (who is online)

# Usage

Example of script launch on Linux (for security reasons, the password entered by the user is not displayed):

```bash

$ python3 vk_friends_online.py
Enter your VK credentials:
Enter login: your_login
Enter password:
------------------------------
   Your VK Friends Online:
------------------------------
Alexander Alexandrov
Ivan Ivanov
Petr Petrov
Sergey Sergeev

```

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
