from base import Plugin


class Whitespace(Plugin):

    def validate_line(self, filename, line_num, line):

        if self.config.get("CHECK_CRLF"):
            if line.endswith(b"\r\n"):
                self.error_callback(filename, line_num, "line ends with CRLF")

        if self.config.get("CHECK_TABS"):
            if b"\t" in line:
                self.error_callback(filename, line_num, "line contains a tab")

        if self.config.get("CHECK_TRAILING_WHITESPACE"):
            if line.rstrip(b"\n").endswith((b" ", b"\t")):
                self.error_callback(filename, line_num, "trailing whitespace")

    def validate_last_line(self, filename, line_num, line):
        if self.config.get("CHECK_NO_EOF_NEWLINE"):
            if not line.endswith(b"\n"):
                self.error_callback(filename, line_num, "no newline at end of file")


plugin = Whitespace
