#!/usr/bin/env bash
set -e

. "build_variables.sh"
. "$BUILD_LIB_DIR/common.sh"
. "$BUILD_LIB_DIR/with_venv.sh"

"$BUILD_SCRIPTS_DIR/analyze_python.sh"

with_venv
python -m nuitka --standalone "$PROJECT_DIR/src/pathfinder_editor/pathfinder_editor.py"
