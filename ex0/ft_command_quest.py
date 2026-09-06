#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    size = len(sys.argv)
    if size < 2:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {size - 1}")
        i = 1
        for current_arg in sys.argv[1:]:
            print(f"Argument {i}: {current_arg}")
            i += 1
    print(f"Total arguments: {size}")
