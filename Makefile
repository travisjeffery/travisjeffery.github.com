.PHONY: build
build:
	@node serve.js

.PHONY: serve
serve:
	@cd build && python3 -m http.server 8000

.PHONY: deploy
deploy: build
	@git checkout master
	@cp -Rf build/* .
	@git clean -Xf
	@git add --all
	@git commit -m 'update'
	@git push
	@git checkout src
