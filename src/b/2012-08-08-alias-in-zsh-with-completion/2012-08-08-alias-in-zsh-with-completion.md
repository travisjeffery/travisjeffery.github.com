---
layout: post.html
title: "Alias in zsh with completion"
date: 2012-08-08 03:56
comments: false
categories: zsh git shell alias completion compdef
---

I use the shell. I use the shell a lot. I type `git` so often it's 
ridiculous. We have shell aliases to make stuff like this a bit shorter, but
often with less functionality. In particular, an alias in itself won't maintain
the completion function, but this is easy to fix:

```sh
alias g=git
compdef g=git
```

And boom! You can now do `g st<TAB>` to complete `status` or whatever,
this technique will also work any other alias/completion function as well.
