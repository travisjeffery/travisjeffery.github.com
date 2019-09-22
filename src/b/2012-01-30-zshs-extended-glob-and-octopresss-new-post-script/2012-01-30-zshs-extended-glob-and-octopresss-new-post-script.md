---
layout: post.html
title: "Zsh's extended glob, and Octopress's new_post script"
date: 2012-01-30 06:44
comments: false
categories: zsh octopress shell
---

If you're here it's because you're a Zsh user, maybe you use Octopress and have
come across the following error (or something similar):

`zsh: no matches found: new_post[...] `

Octopress's documentation is Bash oriented, and so in the example above; the
user would have likely read the documentation and tried something like this:

`$ rake new_post["..."]`

So here's the problem, ...other than you throwing junk into your Zsh configuration
that before understanding what it all meant! ...the problem is that you have
something like this in your `~/.zshrc`, or equivalent file:

`setopt extended_glob`

By setting this option you is turn on all kinds of globbing patterns that Zsh will
expand and match against your files.

For some more in-depth info on Zsh's expansion and globbing, I'd start
[here](http://www.refining-linux.org/archives/37/ZSH-Gem-2-Extended-globbing-and-expansion/),
and then later check out [this](http://zsh.sourceforge.net/Doc/Release/Expansion.html).

So, here are a couple of solutions:

Alias `rake` such that globbing is disabled with:

`alias rake="noglob rake"`

Or always quote arguments given to `rake`:

`rake "new_post[...]"`

Note that I do not have quotes inside my square brackets. This was intentional.
