"""
Main file of AutoAdmin project
"""

import argparse
import github_update
import settings_update

def main():
    #parser description
    parser = argparse.ArgumentParser(description="deploy Django application on webserver")

    #parser module launcher
    parser.add_argument("-g", "--github", action="store_true", help="launch the github module")
    parser.add_argument("-l", "--local", type=str, help="use a local variable file (you can get a copy with '-gl')")
    parser.add_argument("-gl", "--getlocal", action="store_true", help="get a copy of the local variable file")

    #parser mandatory args
    parser.add_argument("path", type=str, help="the path for root of the project (where it should be deployed)")

    #noise level options
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true") #2
    group.add_argument("-q", "--quiet", action="store_true") #0
    noise = 1 #default
    
    #getting args from parser
    args = parser.parse_args()

    if args.quiet:
        noise = 0
    elif args.verbose:
        noise = 2

    if args.github:
        github_update.main(noise)

    if args.getlocal:
        print("Copying the lvar file ...")
        return
    settings_update.main()

if __name__ == "__main__":
    main()