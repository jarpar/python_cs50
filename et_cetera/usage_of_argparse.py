#python usage_of_argparse.py -n 3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")

