#!/bin/bash
ARGUMENTS=( "$@" )
pytest --verbose -m "major and (not slow)" "${ARGUMENTS[*]}"
