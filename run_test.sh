#!/bin/sh
sudo pip install -U pytest
echo "Start run selenium tests for"

if [ $BRANCH_NAME = master ]; then
    export BRANCH_NAME=$TRAVIS_PULL_REQUEST_BRANCH;
    echo $BRANCH_NAME "->master";
else
    echo $TRAVIS_PULL_REQUEST_BRANCH "->" $BRANCH_NAME;
fi

export PATH=$PATH:$(pwd)/drivers
pytest