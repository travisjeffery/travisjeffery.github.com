.PHONY: commit
commit:
	git add --all
	git commit -m update

.PHONY: commit build
build:
	@node serve.js

.PHONY: serve
serve:
	@cd build && URL='' python3 -m http.server 8000

.PHONY: deploy
deploy: build
	@git checkout master
	@cp -Rf build/* .
	@git clean -Xf
	@git add --all
	@git commit -m 'update'
	@git push
	@git checkout src

.PHONY: new
new:
	@cd src/b && touch "$$(date +%F).md"
	@echo "$$(date +%F).md"

.PHONY: all
all: commit build deploy
