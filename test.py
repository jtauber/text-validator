#!/usr/bin/env python3

import glob

from base import Suite

import plugins.whitespace
import plugins.unicode
import plugins.ref_line_format
import plugins.characters


suite = Suite()
suite.add_plugin(plugins.whitespace, {
    "CHECK_CRLF": True,
    "CHECK_TABS": True,
    "CHECK_TRAILING_WHITESPACE": True,
    "CHECK_NO_EOF_NEWLINE": True,
})
suite.add_plugin(plugins.unicode, {
    "CONFIRM_UTF_8_NFD": True,
    "CONFIRM_UTF_8_NFC": True,
})
suite.validate_files(sorted(glob.glob("tests/*.txt")))

suite.add_plugin(plugins.ref_line_format, {
    "REF_REGEX": r"(\d+|EP|SB)\.\d+(\.\d+)?$",  # example from AF
})
suite.add_plugin(plugins.characters, {
    "REPLACE_CHARS": [
        ("\u02BC", "\u2019"),  # bad character, suggested replacement
        ("\u1FBF", "\u2019"),
    ],
})
suite.validate_files([
    "tests/test_0007.txt",
    "tests/test_0008.txt",
    "tests/test_0009.txt",
    "tests/test_0010.txt",
])
