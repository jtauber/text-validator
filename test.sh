#!/bin/sh

validate-text tests/config_001.toml tests/test_0001.txt tests/test_0002.txt tests/test_0003.txt tests/test_0004.txt
validate-text tests/config_002.toml tests/test_0005.txt tests/test_0006.txt
validate-text tests/config_003.toml tests/test_0005.txt tests/test_0006.txt
validate-text tests/config_004.toml tests/test_0007.txt tests/test_0008.txt tests/test_0009.txt
validate-text tests/config_005.toml tests/test_0010.txt
validate-text tests/config_006.toml tests/test_0011.txt
