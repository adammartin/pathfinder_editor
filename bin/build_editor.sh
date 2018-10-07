#!/usr/bin/env bash
set -e

. "$BUILD_LIB_DIR/common.sh"
. "$BUILD_LIB_DIR/with_venv.sh"

"$BUILD_SCRIPTS_DIR/analyze_python.sh"

with_venv
python -m nuitka --follow-imports "$PROJECT_DIR/src/pathfinder_editor/pathfinder_editor.py"
