---
title: "Using git's include for private configuration information (like github tokens)"
date: 2012-03-09T00:00:00Z
tags: ["git"]
aliases:
  - /b/2012/03/using-gits-include-for-private-configuration-information-like-github-tokens/
---
Git added a [feature](https://github.com/git/git/commit/9b25a0b52e09400719366f0a33d0d0da98bbf7b0)
that enables you to split your Git config across multiple files.

I store my dotfiles in a public Git repo but I had to exclude my .gitconfig file because it contained by GitHub access token. With this feature, I have a .gitconfig file that contains the config I'd like public and a .githubconfig file that has the config I don't want public. I add .githubconfig to the .gitignore file to make sure I don't check it in by accident.

[Many people have checked in their GitHub access tokens](https://github.com/search?q=token+path%3A.gitconfig&repo=&langOverride=&start_value=1&type=Code&language=). I hope people will use this feature to prevent that.

## How to use the include directive

You set up your config files like so:

- .gitconfig:

		[include]
		  path = .githubconfig

- .githubconfig:

		[github]
		  user = travisjeffery
		  token = secret!

- .gitignore:

        .githubconfig

The path can be relative from the .gitconfig file or absolute.

You include multiple config files like this:

	[include]
	  path = .githubconfig
	  path = .anotherconfig
	  path = .yetanotherconfig

## What if you've already checked in sensitive info?

If you're one of those people who checked in their GitHub access tokens --- or some other config you don't want public --- then you need a fresh access token and set up your configs files like the previous section so you don't make the same mistake again.

If you have many configs and you can't roll them, then you should purge your config file from your history. This process will rebuild your repo's history, so if other people rely on the repo, they must reclone it. This command purges your .gitconfig file from your history:

    git filter-branch --index-filter 'git rm --cached --ignore-unmatch .gitconfig' --prune-empty -- --all

After purging your .gitconfig, set up your config files like the previous section. You still want to roll your configs as soon as you can because you don't know if someone malicious has already saved them. Read this [page](http://help.github.com/remove-sensitive-data/) for more info on removing sensitive data.

## When you can use it

Git's include directive is in version 1.7.10. If you don't want to wait for the release, you can install the latest:

    git clone git://github.com/gitster/git.git
