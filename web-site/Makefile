.PHONY: clean prep build watch serve upload build_html build_css watch_listen watch_do serve_do

default: build

dist_directory = ./../docs

clean:
	@rm -rf $(dist_directory)/
	@rm -rf ./.sass-cache/
	@rm -f .build-canary

prep:
	@rm -rf $(dist_directory)/*
	@mkdir -p $(dist_directory)/css
	@mkdir -p $(dist_directory)/img
	@mkdir -p $(dist_directory)/js

build_css: $(dist_directory)/css/index.css

$(dist_directory)/css/index.css:
	@scss --style compressed --sourcemap=none ./scss/index.scss ./$(dist_directory)/css/index.css

build: prep
	# copy assets
	@cp -a ./assets/* ./$(dist_directory)/

	# build the css file
	@$(MAKE) build_css

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
	@cd $(dist_directory) && pwd && ./../venv/bin/python3 -m http.server

serve: build
	parallel ::: "$(MAKE) watch_listen" "$(MAKE) watch_do" "$(MAKE) serve_do"

