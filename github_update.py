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

def main():
    print("\nIs your project clone already here ?")

    options = input("\n(y/n/quit) : ")
    options = options.lower()

    if options == "y":
        run("pull")
        print("YES")
        return 0
    elif options == "n":
        print("NO")
        return 0
    elif options == "quit":
        print("QUIT")
        return 1
    else:
        print("\nNot a valid command!")
        print("Use (y/n) or 'quit' if you want to start again.")
        main()