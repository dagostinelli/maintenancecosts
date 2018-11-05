.PHONY: clean prep build watch serve upload build_html build_css watch_listen watch_do serve_do

default: build

venv_directory = ./venv
dist_directory = ./../docs/book
md_directory = ./../book

clean:
	@rm -rf $(venv_directory)/
	@rm -rf $(dist_directory)/
	@rm -rf ./.sass-cache/
	@rm -f .build-canary

prep: $(venv_directory)
	@rm -rf $(dist_directory)/*
	@mkdir -p $(dist_directory)/css
	@mkdir -p $(dist_directory)/img
	@mkdir -p $(dist_directory)/js

$(venv_directory):
	@python3 -m venv venv
	@./venv/bin/pip install git+https://github.com/dagostinelli/spoonbill pyinotify htmlmin

build_html: $(patsubst $(md_directory)/%.md, $(dist_directory)/%.html, $(wildcard $(md_directory)/*.md $(md_directory)/**/*.md))
build_css: $(dist_directory)/css/chapter.css

$(dist_directory)/%.html: $(md_directory)/%.md
	@./venv/bin/spoonbill compile ./templates/ default.json $< | ./venv/bin/htmlmin -s > $@

$(dist_directory)/css/chapter.css:
	@scss --style compressed --sourcemap=none ./scss/chapter.scss ./$(dist_directory)/css/chapter.css

build: prep
	# copy assets
	@cp -a ./assets/* ./$(dist_directory)/

	# build the html pages
	@$(MAKE) build_css
	@$(MAKE) build_html

optimize:
	@mogrify -quality 60% -resize "1000^>" $(dist_directory)/img/*.jpg
	@find ./$(dist_directory)/ -name "*.png" -exec optipng {} +;
	@find ./$(dist_directory)/ -name "*.jpg" -exec jpegoptim {} +;

watch_listen:
	@./venv/bin/python3 -m pyinotify -r -a -e IN_CLOSE_WRITE -c 'touch .build-canary' src/

watch_do:
	touch .build-canary
	@while inotifywait .build-canary; do echo "Change Detected. Building..." && sleep 1 && make build; done;

watch: build
	touch .build-canary
	parallel ::: "$(MAKE) watch_listen" "$(MAKE) watch_do"

serve_do:
	@cd $(dist_directory) && pwd && ./../../web-edition/venv/bin/python3 -m http.server

serve: build
	parallel ::: "$(MAKE) watch_listen" "$(MAKE) watch_do" "$(MAKE) serve_do"

