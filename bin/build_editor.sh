#!/usr/bin/env bash
set -e

. "build_variables.sh"
. "$BUILD_LIB_DIR/common.sh"
. "$BUILD_LIB_DIR/with_venv.sh"

"$BUILD_SCRIPTS_DIR/analyze_python.sh"

with_venv
pyinstaller -w -F --clean "$PROJECT_DIR/src/$PYTHON_PACKAGE_NAME/pathfinder_editor.py"
