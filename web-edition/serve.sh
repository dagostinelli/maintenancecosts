#! /bin/bash

set -e

pushd `pwd`

cd $(dirname $(readlink -f -s "$BASH_SOURCE"))

source venv/bin/activate && cd ../docs && python3 -m http.server

popd
