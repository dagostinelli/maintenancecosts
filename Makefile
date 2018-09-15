.PHONY: clean-venv

default: build

clean-venv:
	@rm -rf venv/
	@rm -rf html/

clean: clean-venv

build:
	./build.sh

watch:
	source venv/bin/activate && python -m pyinotify -v /book
