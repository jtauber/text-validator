# text-validator

pluggable command-line tool for validating the formatting and orthography of text files


You config your validator plugins with a TOML file like:

```
["text_validator.plugins.whitespace"]
CHECK_CRLF = true
CHECK_TABS = true
CHECK_TRAILING_WHITESPACE = true
CHECK_NO_EOF_NEWLINE = true

["text_validator.plugins.unicode"]
CONFIRM_UTF_8_NFC = true

["text_validator.plugins.ref_line_format"]
REF_REGEX = "(\\d+|EP|SB)\\.\\d+(\\.\\d+)?$"  # example from AF

["text_validator.plugins.characters"]
REPLACE_CHARS = [
    # bad character, suggested replacement
    ["\u02BC", "\u2019"],
    ["\u1FBF", "\u2019"],
    ["\u037E", "\u003B"],
    ["\u0387", "\u00B7"],
    ["\u0374", "\u02B9"],
    ["\u03D5", "\u03C6"],
    ["\u03D1", "\u03B8"],
]
```

and they'll validate the texts you give it:

```
tests/test_0001.txt:1:line ends with CRLF
tests/test_0001.txt:2:line ends with CRLF
tests/test_0002.txt:1:no newline at end of file
tests/test_0003.txt:1:line contains a tab
tests/test_0004.txt:1:trailing whitespace
tests/test_0006.txt:1:not NFC
tests/test_0007.txt:2:BLANK LINE
tests/test_0008.txt:1:BAD WHITESPACE
tests/test_0008.txt:2:BAD WHITESPACE
tests/test_0009.txt:4:BAD REFERENCE FORM
tests/test_0009.txt:5:BAD REFERENCE FORM
tests/test_0010.txt:2:29:bad U+02BC; consider replacing with U+2019
tests/test_0010.txt:3:29:bad U+1FBF; consider replacing with U+2019
```

To install:

```
pip install text-validator
```

Then you can either run from the command line:

```
validate-text tests/config_004.toml tests/test_0007.txt tests/test_0008.txt tests/test_0009.txt
```

or programmatically from Python, either with the helper function `validate`:

```
from text_validator.main import validate

validate("tests/config_003.toml", ["tests/test_0005.txt", "tests/test_0006.txt"])
```

or by working directly with a Suite instance:

```
from text_validator.base import Suite

suite = Suite()
suite.load_toml("tests/config_002.toml")
suite.validate_files(["tests/test_0005.txt", "tests/test_0006.txt"])
```

Also see:

* [Plugin Directory](https://github.com/jtauber/text-validator/wiki/Plugin-Directory)
* [How to Write a Plugin](https://github.com/jtauber/text-validator/wiki/How-to-Write-a-Plugin)

