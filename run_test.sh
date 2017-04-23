#!/bin/sh
echo "Start run selenium tests..."
export PATH=$PATH:$(pwd)/drivers




if getopts 'stage' flag; then
  case $flag in
    stage) # Run stage tests
       shift
       python basic_test.py
       ;;
    s) # Run full tests with migrations
       shift
       py.test "$@" --nomigrations
       ;;
  esac
else
  py.test "$@" --nomigrations
fi

export RUN_ENV=DEV