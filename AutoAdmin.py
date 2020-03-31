"""
Main file of AutoAdmin project.
Here is the parser which redirect with good options to the other modules.
"""

import argparse
import set_func
import use_func

def set_f(args):
    set_func.main(args)

def use_f(args):
    use_func.main(args)

def main():
    #parser description
    parser = argparse.ArgumentParser(
        description="Deploy a Django application on a webserver. Start by setting the script with the 'set' option."+
        "Then you can use the 'use' option to make it work.",
        epilog="If you have any questions about the script, feel free to contact a Github contributor of the project.")
    subparsers = parser.add_subparsers()

    #parser for the 'set' command
    parser_set = subparsers.add_parser(
        "set",
        description="Set mode, required before using the script.",
        epilog="If you have any questions about the script, feel free to contact a Github contributor of the project.")
    parser_set.add_argument("-gl", "--getlocal", action="store_true", help="get a copy of the local variable file that you can fill")
    parser_set.add_argument("-gh", "--github", action="store_true", help="launch the github module")
    noise_group = parser_set.add_mutually_exclusive_group()
    noise_group.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
    noise_group.add_argument("-q", "--quiet", action="store_true", help="decrease output verbosity")
    parser_set.set_defaults(func=set_f)

    #parser for the 'use' command
    parser_use = subparsers.add_parser(
        "use",
        description="Use mode, be sure you have used the 'set' mode before.",
        epilog="If you have any questions about the script, feel free to contact a Github contributor of the project.")
    parser_use.add_argument("-p", "--path", type=str, help="the path for root of the project (where it should be deployed)")
    noise_group = parser_use.add_mutually_exclusive_group()
    noise_group.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
    noise_group.add_argument("-q", "--quiet", action="store_true", help="decrease output verbosity")
    parser_use.set_defaults(func=use_f)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()