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
```
