deploy:
	@node serve.js
	@git checkout master
	@cp -Rf build/* .
	@git clean -Xf
	@git add --all
	@git commit -m 'update'
	@git push
	@git checkout src
