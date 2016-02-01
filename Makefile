generate:
	@node serve.js
	@git checkout master
	@cp -Rf build/* .
	@git clean -Xf
