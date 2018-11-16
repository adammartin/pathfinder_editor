#!/usr/bin/env bash
set -e

. "build_variables.sh"
. "$BUILD_LIB_DIR/common.sh"
. "$BUILD_LIB_DIR/with_venv.sh"

"$BUILD_SCRIPTS_DIR/analyze_python.sh"

with_venv
pyinstaller -w -F --clean "$PROJECT_DIR/src/$PYTHON_PACKAGE_NAME/pathfinder_editor.py"

rm -rf "$PROJECT_DIR/pathfinder_editor_win"
mkdir "$PROJECT_DIR/pathfinder_editor_win"
cp -R "$PROJECT_DIR/winpython" "$PROJECT_DIR/pathfinder_editor_win/winpython"
cp -R "$PROJECT_DIR/src/editor" "$PROJECT_DIR/pathfinder_editor_win/editor"
cp -R "$PROJECT_DIR/src/pathfinder_launcher.bat" "$PROJECT_DIR/pathfinder_editor_win/pathfinder_launcher.bat"
cp "$PROJECT_DIR/pathfinder_editor_win/editor/pathfinder_editor.py" "$PROJECT_DIR/pathfinder_editor_win/pathfinder_editor.py"
cd "$PROJECT_DIR/pathfinder_editor_win"
zip -r "$PROJECT_DIR/dist/pathfinder_editor_win.zip" "."
rm -rf "$PROJECT_DIR/build"
rm -rf "$PROJECT_DIR/pathfinder_editor_win"
