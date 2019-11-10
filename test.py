#!/usr/bin/env python3

from text_validator.base import Suite
from text_validator.main import validate

# you can call validate

validate(
    "tests/config_001.toml",
    [
        "tests/test_0001.txt",
        "tests/test_0002.txt",
        "tests/test_0003.txt",
        "tests/test_0004.txt",
    ],
)


# or directly work with a Suite instance:

suite = Suite()
suite.load_toml("tests/config_002.toml")
suite.validate_files(["tests/test_0005.txt", "tests/test_0006.txt"])


validate("tests/config_003.toml", ["tests/test_0005.txt", "tests/test_0006.txt"])
validate(
    "tests/config_004.toml",
    ["tests/test_0007.txt", "tests/test_0008.txt", "tests/test_0009.txt"],
)
validate("tests/config_005.toml", ["tests/test_0010.txt"])
