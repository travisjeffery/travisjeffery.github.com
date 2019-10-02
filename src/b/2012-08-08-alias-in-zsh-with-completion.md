---
layout: post.html
title: "Alias in ZSH with completion"
date: 2012-08-08 03:56
comments: false
collection: zsh
---

I use git in a terminal all day, every day. 3 characters adds up if you type them enough, `g i t`, so let's shorten what we have to type.

You shorten a command by making a shorter alias. So I alias `g` to `git`:

    alias g=git

I like terminal commands with completion, especially a command like git with a many, long arguments. Aliases do not automatically assume the original command's completion. Here's how we add completion to our alias:

    compdef g=git

And boom! You can do `g st<TAB>` to complete `status`. The `compdef` makes the g alias complete as if ZSH was completing git instead.

Now I git away by typing `g`.
