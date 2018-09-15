#! /bin/bash

pushd `pwd`

cd $(dirname $(readlink -f -s "$BASH_SOURCE"))

if [ ! -d "venv" ]; then
	python3 -m venv venv
	source venv/bin/activate
	pip install jinja2 beautifulsoup4 markdown smartypants pyinotify
	deactivate
fi

source venv/bin/activate && rm -rf html && python3 build.py

popd