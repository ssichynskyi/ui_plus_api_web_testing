#!/bin/bash
ARGUMENTS=( "$@" )
pytest --maxfail=0 --verbose -m critical "${ARGUMENTS[*]}"
