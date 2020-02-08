import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--func-to-run', default='auto_run')
parser.add_argument('-b', '--bar-value', default=3.14)
args = parser.parse_args()

print(args.my_foo)