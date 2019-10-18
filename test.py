#!/usr/bin/env python3

import glob
import sys

import plugins.whitespace
import plugins.unicode


def error_callback(filename, line_num, error):
    print(f"{filename}:{line_num}:{error}", file=sys.stderr)


PLUGINS = [
    plugins.whitespace.plugin(error_callback, {
        "CHECK_CRLF": True,
        "CHECK_TABS": True,
        "CHECK_TRAILING_WHITESPACE": True,
        "CHECK_NO_EOF_NEWLINE": True,
    }),
    plugins.unicode.plugin(error_callback, {
        "CONFIRM_UTF_8_NFD": True,
        "CONFIRM_UTF_8_NFC": True,
    })
]


for filename in sorted(glob.glob("tests/*.txt")):
    with open(filename, "rb") as f:

        line_num = 0
        for line in f:
            line_num += 1
            for plugin in PLUGINS:
                if line_num == 1:
                    plugin.validate_first_line(filename, line_num, line)
                plugin.validate_line(filename, line_num, line)
        for plugin in PLUGINS:
            plugin.validate_last_line(filename, line_num, line)
