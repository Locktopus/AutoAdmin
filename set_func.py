"""
Main file for the settings function.
args can contain :
  -gl, --getlocal  get a copy of the local variable file that you can fill
  -gh, --github    launch the github module
  -v, --verbose    increase output verbosity
  -q, --quiet      decrease output verbosity
"""

def main(args):
    print(args.getlocal)
    