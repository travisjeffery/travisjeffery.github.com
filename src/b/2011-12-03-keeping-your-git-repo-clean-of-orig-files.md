---
layout: post.html
title: "Keeping your git repo clean of .orig files!"
date: 2011-12-03 17:19
comments: false
collection: git
---

For teams building projects with git, a good habit is to rebase and merge often so conflicts are
less frequent and easier to resolve. Also, this helps keeps your branching hierarchy simple. When
people have to make complicated merges, it's often because their branching hierarchy is complex.

Keep things simple!

This post's topic: How to clean up .orig files that have built up in your project's repository from merges.

1. git clean

	`git clean` removes untracked files from the working tree of your project. You'll usually run it
	like so:

	    git clean -fd

	`git clean` won't even remove any files unless you give it the
	`-f` argument and `-d` tells git to remove the directories that aren't under version
	control --- along with the files.

    With the `-n` arg, `git clean` will do a dry-run and show you what it will remove:

	    git clean -nd

2. Configure your mergetool

	You can configure you mergetool to not preserve the .orig files, however
	not all Git mergetool's support this feature and some still preserve the .orig files
	even with this configuration:

	    git config --global mergetool.keepBackup false

3. Just ignore them!

	Add this to your project's .gitignore file:

	    *.orig

	With this setup, you don't have to worry about checking these files into your repo. The files will still be on your disk though, and when you want to clean them you'll need to pass the `-x` arg:

	    git clean -fdx

If you have files ignored that you need
for your Development environment e.g. tags, logs, or config files then make sure you stipulate the path you want cleaned so the files you need aren't removed:

    git clean -fdx app
