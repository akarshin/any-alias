import re
import os
import sys
import yaml
from a.Helper import Helper


class A(object):
    _argument_dict = {}
    _argument_list = []
    _settings = {}

    # Run a command
    def run(self, command, arguments):
        # 2. Parse arguments to dictionary and list. Dictionary are for named variables, list is for anonymous ones.
        # 3. Substitute certain reserved constants, named variables and then anonymous variables.

        self._load_config_files()
        self._validate_config_version()
        self._separate_arguments(arguments)
        self._initiate_run(command)

    # Reparse and return settigns
    def get_settings(self):
        self._load_config_files()
        self._validate_config_version()

        return self._settings

    # Load all the config files into one dictionary
    def _load_config_files(self):
        default_settings = {}
        local_settings = {}

        try:
            default_settings = self._load_config_file(os.path.dirname(__file__))
        except FileNotFoundError:
            print("Can't locate native alias.yml file, the app is corrupt. Please reinstall.")
            sys.exit()

        cwd_list = os.getcwd().split('/')

        while not cwd_list == ['']:
            path = "/".join(cwd_list)

            try:
                local_settings = self._merge_settings(local_settings, self._load_config_file(path))
            except FileNotFoundError:
                pass

            cwd_list = cwd_list[:-1]

        self._settings = self._merge_settings(default_settings, local_settings)

    # Load a specific config file from specific location
    def _load_config_file(self, path):
        with open(path + "/alias.yml", "r") as stream:
            try:
                return yaml.load(stream)
            except yaml.YAMLError as ex:
                print(ex)
                sys.exit()

    # Merge the settings so that all of them are available.
    def _merge_settings(self, source, destination):
        for key, value in source.items():
            if isinstance(value, dict):
                node = destination.setdefault(key, {})
                self._merge_settings(value, node)
            else:
                destination[key] = value

        return destination

    # Parse arguments to dictionary and list. Dictionary is for named variables, list is for anonymous ones.
    def _separate_arguments(self, arguments):
        prepared_dict = []

        for argument in arguments:
            match = re.match(r"--([\w]+)=([\w\s]+)", argument)

            if match:
                prepared_dict.append((match.group(1), match.group(2)))
            else:
                self._argument_list.append(argument)

        self._argument_dict = dict(prepared_dict)

    # Die if yaml file version is not supported
    def _validate_config_version(self):
        if self._settings['version'] > self._settings['supported_version']:
            print("alias.yml version is not supported")
            sys.exit()

    # Prepare and run specific command
    def _initiate_run(self, command_name):
        try:
            command_list = self._settings['commands'][command_name]
            argument_list_cycler = iter(self._argument_list)

            # Replace a variable name with either a value from argument dictionary or from argument list
            def replace_variable_match(match):
                try:
                    return self._argument_dict[match.group(1)]
                except KeyError:
                    return next(argument_list_cycler)

            # Replace and
            def run_command(command):
                command = re.sub(r"%%([a-z_]+)%%", replace_variable_match, command)
                os.system(command)

            if isinstance(command_list, str):
                run_command(command_list)
            elif isinstance(command_list, list):
                for command in command_list:
                    run_command(command)
            else:
                Helper(self._settings)
        except StopIteration:
            print("FATAL: You did not specify the variable value for your command.")
            sys.exit()
        except IndexError:
            Helper(self._settings)
            sys.exit()
        except KeyError:
            Helper(self._settings)
            sys.exit()
