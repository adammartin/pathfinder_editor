#!/usr/bin/env bash
set -e

. "$BUILD_LIB_DIR/common.sh"
. "$BUILD_LIB_DIR/with_venv.sh"

MIN_COVERAGE_PERCENTAGE=90

with_venv
pushd_silent "$PROJECT_DIR"
echo "Running pytest"
pytest --cov="$PYTHON_PACKAGE_NAME" --junit-xml="test_results.xml"
echo "Generating coverage report"
coverage xml
coverage report --fail-under "$MIN_COVERAGE_PERCENTAGE" --skip-covered
popd_silent
