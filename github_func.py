"""
File that contain all the github functions.
"""

import subprocess

def run(*args):
    return subprocess.check_call(['git'] + list(args))

def clone():
    user = input("User: ")
    __user__ = f'{user}'
    repo = input("Repository: ")
    __repo__ = f'{repo}'

    subprocess.Popen(['git', 'clone', "https://github.com/" + __user__ + "/" + __repo__ + ".git"])