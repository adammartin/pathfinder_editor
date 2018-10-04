#!/usr/bin/env bash
set -e

"$BUILD_SCRIPTS_DIR/analyze_python.sh"
"$BUILD_SCRIPTS_DIR/run_unit_tests.sh"
