---
layout: post.html
title: "Keeping your git repo clean of .orig files! "
date: 2011-12-03 17:19
comments: false
categories: git automation rebase
---

For teams building projects with git, a good habit is to rebase and merge
often. This way, conflicts are less frequent and easier to resolve. Also, this
helps keeps your branching hierarchy simpler. When people have trouble with
git, often it's because their branching hierarchy has become complex.

Keep things simple!

This post's topic: how to clean up .orig files that may occur and build-up in
your project's repository.

1. `git clean`

	One command that you'll find quite useful is `git clean`, it removes untracked
	files from the working tree of your project. Most often you'll use it like so:

	    git clean -fd


	The reason for this is that `git clean` won't even run unless you give it the
	`-f` argument and `-d` will also remove directories that not under version
	control.

	Another useful argument is `-n` which will do a dry-run and show you what would
	be removed:

	    git clean -nd

2. Configure your mergetool

	You can also configure you mergetool to not preserve the .orig files, however
	not all Git mergetool's support this feature and still preserve the .orig files
	even with this configuration:

	    git config --global mergetool.keepBackup false

3. Just ignore them!

	Add this to your project's .gitignore file:

	    *.orig

	This is the most simplest of all solutions and ultimately probably the best, if
	this what you choose to do the `git clean` will still be able to clean them but
	you will have to invoke it with the `-x` argument:

	    git clean -fdx

If you're already ignoring a lot of files or have files ignored that you need
for your Development environment e.g. tags, logs, or config files then you just
need to stipulate the path you want cleaned so they aren't removed:

    git clean -fdx app


