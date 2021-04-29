#!/bin/bash
ARGUMENTS=( "$@" )
pytest --verbose -m "minor and slow" "${ARGUMENTS[*]}"
