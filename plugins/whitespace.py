from base import Plugin


class Whitespace(Plugin):

    def validate_line(self, filename, line_num, line):

        def error(message):
            self.error_callback(filename, line_num, message)

        if self.config.get("CHECK_CRLF"):
            if line.endswith(b"\r\n"):
                error("line ends with CRLF")

        if self.config.get("CHECK_TABS"):
            if b"\t" in line:
                error("line contains a tab")

        if self.config.get("CHECK_TRAILING_WHITESPACE"):
            if line.rstrip(b"\n").endswith((b" ", b"\t")):
                error("trailing whitespace")

    def validate_last_line(self, filename, line_num, line):

        def error(message):
            self.error_callback(filename, line_num, message)

        if self.config.get("CHECK_NO_EOF_NEWLINE"):
            if not line.endswith(b"\n"):
                error("no newline at end of file")


plugin = Whitespace
