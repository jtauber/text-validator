#!/usr/bin/env python3

import argparse

from .base import Suite


def validate(config, files):
    suite = Suite()
    suite.load_toml(config)
    suite.validate_files(files)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("config", help="toml file configuring validator plugins")
    parser.add_argument("files", nargs="+", help="file(s) to validate")
    args = parser.parse_args()

    validate(args.config, args.files)


if __name__ == "__main__":
    main()
