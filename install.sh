#!/usr/bin/env bash

uname="$(uname -s)"

case "${uname}" in
  Linux*)
    pip3 install --user --force-reinstall --upgrade .
    ;;
  Darwin*)
    predefined_target_path=""
    display_predefined_target_path=""

    if [ -f install.lock ]; then
      predefined_target_path="`cat install.lock`"
      display_predefined_target_path=" [${predefined_target_path}]"
    fi

    echo "Path to install to${display_predefined_target_path}:"
    read target_path

    if [ "$target_path" == "" ]; then
      target_path="$predefined_target_path"
    else
      echo "${target_path}" > install.lock
    fi

    pip3 install --target "${target_path}" --force-reinstall --upgrade .
    ;;
  *)
    echo "FATAL: Could not figure out your OS. It doesn't look like Linux or MacOS."
esac
