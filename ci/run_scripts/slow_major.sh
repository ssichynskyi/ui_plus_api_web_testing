#!/bin/bash
ARGUMENTS=( "$@" )
pytest --verbose -m "major and slow" "${ARGUMENTS[*]}"
