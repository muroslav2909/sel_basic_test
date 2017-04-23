#!/bin/sh
sudo pip install -U pytest
echo "Start run selenium tests for"
echo $BRANCH_NAME
export PATH=$PATH:$(pwd)/drivers
pytest

