"""
Main file for the settings function.
args can contain :
  -gl, --getlocal  get a copy of the local variable file that you can fill
  -gh, --github    launch the github module
  -v, --verbose    increase output verbosity
  -q, --quiet      decrease output verbosity
"""

import shutil
import github_func

def main(args):
  #noise introduction
  if args.verbose:
    print("\nSet mode activated, launching options module ...")
  elif args.quiet is False:
    print("\nSet mode")

  #getlocal option
  if args.getlocal:
    shutil.copy("./lvar_exemple.py","./custom_lvar.py")
    if args.verbose:
      print("\ngetlocal options :\n"+
      "Local variable file have been copied.\n"+
      "Now you have a file 'custom_lvar.py' that you can fill with your local variable.")
    elif args.quiet is False:
      print("\ngetlocal options :\n"+
      "Local variable file have been copied.")
  
  #github option
  if args.github:
    if args.verbose:
      print("\ngithub options :\n"+
      "You'll be asked to enter whatever github options you need to use.")
    elif args.quiet is False:
      print("\ngithub options :\n")
    #git clone
    print("Do you need a git clone ?")
    prompt = input("\ny/n : ")
    prompt = prompt.lower()
    if prompt == "y":
      if args.verbose or args.quiet is False:
        print("\nYou will be asked for the user first and then the repository name\n")
      github_func.clone()
    #other git options
    print("Do you need an other git options (pull/push/status/diff/show) ?")
    prompt = input("\n'options' or 'n': ")
    prompt = prompt.lower()
    if prompt != "n":
      github_func.run(prompt)

  #noise exit
  if args.verbose or args.quiet is False:
    print("\nEnd of set mode.")