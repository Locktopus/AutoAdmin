"""
Main file for the using function.
args can contain :
  -p PATH, --path PATH  the path for root of the project (where it should be deployed)
  -v, --verbose         increase output verbosity
  -q, --quiet           decrease output verbosity
"""

import settings_update
import os

def main(args):
  #noise introduction
  if args.verbose:
    print("\nUse mode activated, launching options module ...")
  elif args.quiet is False:
    print("\nUse mode")
  
  #error management
  error = True

  if args.path and (args.path == os.getcwd()):
    if args.verbose or args.quiet is False:
      print("You are in the good directory to execute the script.")
  else:
    if args.verbose or args.quiet is False:
      print("You are in the wrong directory to execute the script."+
      "\nYou should be on", args.path, "and you are on", os.getcwd())
      error = False

  if error:
    settings_update.main()
    if args.verbose:
      print("\nYour setting file has been updated (and potentially copied).")
    elif args.quiet is False:
      print("\nFile updated.")

  #noise exit
  if args.verbose or args.quiet is False:
    print("\nEnd of use mode.")