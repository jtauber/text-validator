import sys


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


def error_callback(filename, line_num, error):
    print(f"{filename}:{line_num}:{error}", file=sys.stderr)


class Suite:

    def __init__(self):
        self.plugins = []

    def add_plugin(self, module, config):
        self.plugins.append(module.plugin(error_callback, config))

    def validate_files(self, filenames):
        for filename in filenames:
            with open(filename, "rb") as f:
                line_num = 0
                for line in f:
                    line_num += 1
                    for plugin in self.plugins:
                        if line_num == 1:
                            plugin.validate_first_line(filename, line_num, line)
                        plugin.validate_line(filename, line_num, line)
                for plugin in self.plugins:
                    plugin.validate_last_line(filename, line_num, line)