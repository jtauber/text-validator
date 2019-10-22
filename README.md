# text-validator

pluggable command-line tool for validating the formatting and orthography of text files


Soon this will be configurable by config file but for now, to give you a flavour, you set up a suite of validator plugins:

```
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
```

and they'll validate the texts you give it:

```
tests/test_0001.txt:1:line ends with CRLF
tests/test_0001.txt:2:line ends with CRLF
tests/test_0002.txt:1:no newline at end of file
tests/test_0003.txt:1:line contains a tab
tests/test_0004.txt:1:trailing whitespace
tests/test_0005.txt:1:not NFD
tests/test_0006.txt:1:not NFC
tests/test_0007.txt:2:BLANK LINE
tests/test_0008.txt:1:BAD WHITESPACE
tests/test_0008.txt:2:BAD WHITESPACE
tests/test_0009.txt:4:BAD REFERENCE FORM
tests/test_0009.txt:5:BAD REFERENCE FORM
tests/test_0010.txt:2:29:bad U+02BC; consider replacing with U+2019
tests/test_0010.txt:3:29:bad U+1FBF; consider replacing with U+2019
```
