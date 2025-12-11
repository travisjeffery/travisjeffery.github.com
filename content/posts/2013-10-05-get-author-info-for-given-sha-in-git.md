---
title: "`git author sha`: get author info for a given sha in git"
date: 2013-10-05T00:00:00Z
tags: ["git"]
aliases:
  - /b/2013/10/git-author-sha-get-author-info-for-a-given-sha-in-git/
---
When i'm hacking on open source libs i maintain, i often have to clean up the
commits of people's prs. I wanna give attribution for good contributions and
not have my name associated with nasty hacks, so when i interactively rebase
commits i want to make sure the new commit(s) has the right author.

By default when you interactively rebase, git will say you're the author. So
you need to explicitly set this otherwise.

`git commit -a -m 'some shit (fixes #99) --author="rza <rza@wu-tang.xxx>"'`

But getting that author info is a little annoying, involving logging the old
commit(s), then copying and pasting the author info. So I wrote `git author sha`.

`git author HEAD` writes `rza <rza@wu-tang.xxx>`.

Now I can do:

`git commit -a -m 'some shit (fixes #99) --author="$(git author sha)"`

Here's `git author` in my [.gitconfig](https://github.com/travisjeffery/dotfiles/blob/master/.gitconfig):

```
[alias]
  author = "!sh -c 'echo $(git log -1 --format=\"%an <%ae>\" $@) | tr -d \"\\n\"'" -"'"
```
