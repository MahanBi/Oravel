from argparse import ArgumentParser
from main import Initializer


def main():
    parser = ArgumentParser()
    parser.add_argument("run", choices=['test', 'build'], help='run Oravel')
    parser.add_argument("--version", action="store_true", help='Oravel Version')
    args = parser.parse_args()

    if args.run:
        Initializer()

    elif args.version:
        print("0.0.0")


if __name__ == "__main__":
    main()
