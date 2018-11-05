.PHONY: clean build

default: build

clean:
	@cd ./web-edition && $(MAKE) clean

build:
	@cd ./web-edition && $(MAKE) build

