#!/usr/bin/env python3

import glob

from base import Suite

import plugins.whitespace
import plugins.unicode

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
