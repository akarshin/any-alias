#!/usr/bin/env bash

uname="$(uname -s)"

case "${uname}" in
  Linux*)
    pip3 install --user --force-reinstall --upgrade .
    ;;
  Darwin*)
    pip3 install --user --force-reinstall --upgrade .
    sudo ln -s ~/Library/Python/3.6/bin/a /usr/local/bin/a

    echo "Your python installation directory might be root only."
    echo "If Any Alias does not work on your system, try reassigning the python installation directory to your user"
    echo "by running 'sudo chown $USER ~/Library/Python'"
    ;;
  *)
    echo "FATAL: Could not figure out your OS. It doesn't look like Linux or MacOS."
esac
