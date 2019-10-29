#!/usr/bin/env python3

from base import Suite

suite = Suite()
suite.load_toml("tests/config_001.toml")
suite.validate_files(
    [
        "tests/test_0001.txt",
        "tests/test_0002.txt",
        "tests/test_0003.txt",
        "tests/test_0004.txt",
    ]
)

suite = Suite()
suite.load_toml("tests/config_002.toml")
suite.validate_files(["tests/test_0005.txt", "tests/test_0006.txt"])

suite = Suite()
suite.load_toml("tests/config_003.toml")
suite.validate_files(["tests/test_0005.txt", "tests/test_0006.txt"])

suite = Suite()
suite.load_toml("tests/config_004.toml")
suite.validate_files(
    ["tests/test_0007.txt", "tests/test_0008.txt", "tests/test_0009.txt"]
)

suite = Suite()
suite.load_toml("tests/config_005.toml")
suite.validate_files(["tests/test_0010.txt"])
