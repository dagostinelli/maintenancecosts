.PHONY: clean build

default: build

clean:
	@rm -rf docs/
	@cd ./web-edition && $(MAKE) clean
	@cd ./web-site && $(MAKE) clean

build:
	@cd ./web-site && $(MAKE) build
	@cd ./web-edition && $(MAKE) build

