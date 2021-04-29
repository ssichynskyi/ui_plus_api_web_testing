#!/bin/bash
ARGUMENTS=( "$@" )
pytest --maxfail=0 --verbose -m "minor and (not slow)" "${ARGUMENTS[*]}"
