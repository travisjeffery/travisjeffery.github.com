---
layout: post.html
title: "Using git's include for private configuration information (like github tokens)"
date: 2012-03-09 03:21
comments: false
collection: git
---

Recently Git added an [amazingly needed feature](https://github.com/git/git/commit/9b25a0b52e09400719366f0a33d0d0da98bbf7b0),
include for gitconfig files.

This means that you can split your gitconfig configurations across multiple
files, e.g. you can have a .gitconfig file for your nonsensitive information and a
git ignored .githubconfig file containing your private github token.

Storing GitHub tokens doesn't [seem to be](https://github.com/search?q=token+path%3A.gitconfig&repo=&langOverride=&start_value=1&type=Code&language=)
all that uncommon, so hopefully with Git's include feature this will change.

This what you'll have in your .gitconfig file:

```
[include]
  path = .githubconfig
```

And in your .githubconfig file:

```
[github]
  user = travisjeffery
  token = secret!
```

Then in your .gitignore file have:

```
.githubconfig
```

As an aside, to include multiple config files the directive is the same:

```
[include]
  path = .githubconfig
  path = .anotherconfig
  path = .yetanotherconfig
```

The path can be either relative from the gitconfig file or absolute.

If you've been silly enough to have put sensitive information into your
gitconfig on the assumption it wouldn't come back at you, now Git has the
functionality so use it!

Read this [page](http://help.github.com/remove-sensitive-data/) on how to purge
a file from your history.

Purge your gitconfig file from your history (below), put the sensitive information into
another file that you've git ignored, include that file in your gitconfig and
add your newly desensitized gitconfig back under version control.

```
git filter-branch --index-filter 'git rm --cached --ignore-unmatch .gitconfig' --prune-empty -- --all
```

Git's include will be in version 1.7.10, but if you don't want to wait
homebrewers will [soon](https://github.com/mxcl/homebrew/pull/10806) be able to easily
install Git's latest development version via:

`brew install git --HEAD`

Or just git the repo and build it yourself:

`git clone git://github.com/gitster/git.git`
