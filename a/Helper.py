class Helper(object):
    settings = {}

    def __init__(self, settings):
        self.settings = settings
        self.print_helper()

    def _print_header(self):
        bold_start = "\033[1m"
        bold_end = "\033[0;0m"

        print("""
                                         _ _
            /\                     /\   | (_)
           /  \   _ __  _   _     /  \  | |_  __ _ ___
          / /\ \ | '_ \| | | |   / /\ \ | | |/ _` / __|
         / ____ \| | | | |_| |  / ____ \| | | (_| \__ \\
        /_/    \_\_| |_|\__, | /_/    \_\_|_|\__,_|___/
                         __/ |
                        |___/

        """ + bold_start + """DESCRIPTION:""" + bold_end + """
          Any Alias - Developer's time saver.
        """)

    def _print_commands(self):
        bold_start = "\033[1m"
        bold_end = "\033[0;0m"

        for key, commands in (self.settings['commands']).items():
            if isinstance(commands, str):
                print((" " * 10) + bold_start + key + bold_end)
                print((" " * 12) + commands)
            if isinstance(commands, list):
                print((" " * 10) + bold_start + key + bold_end)
                for command in commands:
                    print((" " * 12) + command)

    def print_helper(self):
        bold_start = "\033[1m"
        bold_end = "\033[0;0m"

        self._print_header()

        print("""
        """ + bold_start + """USAGE:""" + bold_end + """
          """ + bold_start + """a <command>""" + bold_end + """

        """ + bold_start + """COMMANDS:""" + bold_end)

        self._print_commands()