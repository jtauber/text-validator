from text_validator.base import Plugin


class Characters(Plugin):
    def validate_line(self, filename, line_num, line):
        def error(message, offset=None):
            self.error_callback(filename, line_num, offset, message)

        encoding = self.config.get("ENCODING", "utf-8")
        decoded_line = line.decode(encoding)

        for i, char in enumerate(decoded_line, 1):
            for bad_char, suggested_char in self.config.get("REPLACE_CHARS", []):
                if char == bad_char:
                    error(
                        f"bad U+{ord(bad_char):04X};"
                        f"consider replacing with U+{ord(suggested_char):04X}",
                        i,
                    )


plugin = Characters
