#!/usr/bin/env bash
set -e

. "$BUILD_LIB_DIR/common.sh"
. "$BUILD_LIB_DIR/with_venv.sh"

PACKAGE_SOURCE="src/$PYTHON_PACKAGE_NAME"

run_pylint () {
    pylint --rcfile=.pylintrc "src/$PYTHON_PACKAGE_NAME"
}

with_venv
pushd_silent "$PROJECT_DIR"
echo "Running pylint"
run_pylint
echo "Running flake8"
flake8 "$PACKAGE_SOURCE"
echo "Running bandit"
bandit -x "$PACKAGE_SOURCE/_version.py" -r "$PACKAGE_SOURCE"
popd_silent
