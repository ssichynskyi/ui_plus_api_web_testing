#!/bin/bash
ARGUMENTS=( "$@" )
pytest --verbose -m "minor and (not slow)" "${ARGUMENTS[*]}"
