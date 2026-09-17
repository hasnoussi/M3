#!/usr/bin/env python3

import sys

def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    arguments = sys.argv[1:]

    if len(arguments) == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(arguments)}")
        index = 1
        for argument in arguments:
            print(f"Argument {index}: {argument}")
            index += 1

    print(f"Total arguments: {len(sys.argv)}")