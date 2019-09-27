---
layout: post.html
title: "ZSH's extended glob breaking commands"
date: 2012-01-30 06:44
comments: false
collection: zsh
---

After running a command like `$ rake new_post["hello world"]`, you may have seen an error like the following:

```
zsh: no matches found: new_post[...]
```

The issue is that you have ZSH's extended glob turned on. If you look in your ZSH config you'll see the following line:

```
setopt extended_glob
```

This options enables globbing patterns in ZSH. And in the previous example, the `["hello world"]` in
`$ rake new_post["hello world"]` acts like a regexp rather than a literal string. For more info,
this [blog](https://www.refining-linux.org/archives/37-ZSH-Gem-2-Extended-globbing-and-expansion.html)
introduces ZSH globbing and expansion, and this
[page](http://zsh.sourceforge.net/Doc/Release/Expansion.html) comprehensively documents globbing and expansion.

You have a couple ways to fix this problem and I prefer the first way:

- Disable globbing by aliasing the command, for example:
    ```
    alias rake="noglob rake"
    ```
- Quote the command's arguments:
    ```
    rake 'new_post["hello world"]'
    ```
Till next time, keep calm and ZSH on.
