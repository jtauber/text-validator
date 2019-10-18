import unicodedata

from base import Plugin


class Unicode(Plugin):

    def validate_line(self, filename, line_num, line):

        def error(message):
            self.error_callback(filename, line_num, message)

        utf_8_line = line.decode("utf-8")

        if self.config.get("CONFIRM_UTF_8_NFC"):
            if utf_8_line != unicodedata.normalize("NFC", utf_8_line):
                error("not NFC")

        if self.config.get("CONFIRM_UTF_8_NFD"):
            if utf_8_line != unicodedata.normalize("NFD", utf_8_line):
                error("not NFD")


plugin = Unicode
