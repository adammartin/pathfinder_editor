#!/usr/bin/env bash

pushd_silent () {
    pushd "$1" 1> /dev/null
}

popd_silent () {
    popd 1> /dev/null
}
