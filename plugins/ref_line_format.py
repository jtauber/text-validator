import re
import unicodedata

from base import Plugin


class RefLineFormat(Plugin):

    def validate_line(self, filename, line_num, line):

        def error(message):
            self.error_callback(filename, line_num, message)

        l = line.decode("utf-8")
        parts = l.strip().split()

        # there can be no blank lines

        if not parts:
            error("BLANK LINE")

        # tokens must be split by a single space

        if parts and l != " ".join(parts) + "\n":
            error("BAD WHITESPACE")

        # the first token must be a reference of the form given in the
        # REF_REGEX config var

        if parts and not re.match(self.config.get("REF_REGEX", ""), parts[0]):
            error("BAD REFERENCE FORM")


plugin = RefLineFormat
