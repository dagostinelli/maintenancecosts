#! /bin/bash

pushd `pwd`

cd $(dirname $(readlink -f -s "$BASH_SOURCE"))

if [ ! -d "venv" ]; then
	python3 -m venv venv
	source venv/bin/activate
	pip install jinja2 beautifulsoup4 markdown smartypants pyinotify
	deactivate
fi

rm -rf ../docs/*
source venv/bin/activate && python3 build.py
cp -a assets/* ../docs/

popd