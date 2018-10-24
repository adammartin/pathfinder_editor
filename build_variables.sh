#!/usr/bin/env bash

set_dirs () {
    local this_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

    export PROJECT_DIR="$this_dir"
    export BUILD_SCRIPTS_DIR="$this_dir/bin"
    export BUILD_LIB_DIR="$BUILD_SCRIPTS_DIR/build_lib"
}

set_dirs

export PYTHON_FOR_VENV=python3.6
export PYTHON_PACKAGE_NAME='editor'
