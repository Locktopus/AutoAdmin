"""
Main file of AutoAdmin project
"""

import github_update
import settings_update

def main():
    error = 0

    print("\nLaunching script ...")

    choose_command =  input("\nDo you need to clone or update your repo from github ? (y/n) : ")
    choose_command = choose_command.lower()
    if choose_command == "y":
        error = github_update.main()
        if error != 0:
            main()
        print("\nUpdating settings.py to production standards ...")
    elif choose_command == "n":
        print("\nUpdating settings.py to production standards ...")
    else:
        print("\nNot a valid command!")
        print("Use (y/n) or 'quit' if you want to start again.")
        main()

    settings_update.main()
main()