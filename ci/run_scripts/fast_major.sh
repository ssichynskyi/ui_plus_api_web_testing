#!/bin/bash
ARGUMENTS=( "$@" )
pytest --maxfail=0 --verbose -m "major and (not slow)" "${ARGUMENTS[*]}"
