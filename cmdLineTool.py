# python argparse module

import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple cmd line input")
    parser.add_argument("name", help="Your name")
    parser.add_argument("--age", help="Yuur Age")
    args = parser.parse_args()

    print(f"Hello {args.name}! You are {args.age} years old.")

if __name__ == "__main__":
    main()