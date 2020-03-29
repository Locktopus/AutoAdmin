#Getting the latest code from GitHub

import subprocess

def run(*args):
    return subprocess.check_call(['git'] + list(args))

def clone():
    print("\nYou will be asked for the user first and then the repository name\n")

    user = input("User: ")
    __user__ = f'{user}'
    repo = input("Repository: ")
    __repo__ = f'{repo}'

    subprocess.Popen(['git', 'clone', "https://github.com/" + __user__ + "/" + __repo__ + ".git"])

def main(noise):
    print("\nIs your project clone already here ?")

    options = input("\n(y/n) : ")
    options = options.lower()

    if options == "y":
        run("pull")
        if noise in (1, 2):
            print("A git pull have been performed")
        return
    elif options == "n":
        clone()
        if noise in (1, 2):
            print("A git clone have been performed")
        return
    else:
        print("\nNot a valid command!")
        print("Use yes or no (y/n)")
        main(noise)