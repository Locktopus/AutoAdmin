"""
Main file for the using function.
args can contain :
  -p PATH, --path PATH  the path for root of the project (where it should be deployed)
  -v, --verbose         increase output verbosity
  -q, --quiet           decrease output verbosity
"""

def main(args):
    print(args.path)
    