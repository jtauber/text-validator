class Plugin:

    def __init__(self, error_callback, config):
        self.config = config
        self.error_callback = error_callback

    def validate_line(self, filename, line_num, line):
        pass

    def validate_first_line(self, filename, line_num, line):
        pass

    def validate_last_line(self, filename, line_num, line):
        pass
