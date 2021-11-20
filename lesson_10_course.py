# CLI, argparse
import sys

params = sys.argv
print(f"Hello, {params[1]}!", params)

from argparse import ArgumentParser

args = ArgumentParser()

args.add_argument("--name", type=str, default="Vova")
args.add_argument("--age", type=int, default=42, help="Введи целое число")
args.add_argument("-f", "--flag", type=bool, default=True)
args = vars(args.parse_args())
print(args)