#!/bin/sh
echo "Start run selenium tests..."
echo $BRANCH_NAME
export PATH=$PATH:$(pwd)/drivers
python basic_test.py

