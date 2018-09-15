.PHONY: clean-venv

default: buildwebedition

clean-venv:
	@rm -rf ./web-edition/venv/

clean: clean-venv

buildwebedition:
	./web-edition/build.sh

watch:
	./web-edition/watch.sh

serve: buildwebedition
	./web-edition/serve.sh
