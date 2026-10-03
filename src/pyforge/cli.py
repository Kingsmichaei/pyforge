import argparse

from .system import get_system_info


def main():
    parser = argparse.ArgumentParser(
        prog="pyforge",
        description="A Python developer toolkit",
    )

    subparsers = parser.add_subparsers(dest="command")

    info_parser = subparsers.add_parser(
        "info",
        help="Display system information",
    )

    args = parser.parse_args()

    if args.command == "info":
        system_info = get_system_info()

        for key, value in system_info.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()