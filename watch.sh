#! /bin/bash

pushd `pwd`

cd $(dirname $(readlink -f -s "$BASH_SOURCE"))

source venv/bin/activate && python3 watch.py

popd
