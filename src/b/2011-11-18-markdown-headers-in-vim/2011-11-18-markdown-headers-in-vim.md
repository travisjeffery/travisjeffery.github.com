---
layout: post.html
title: "Markdown headers in vim"
date: 2011-11-18 02:06
comments: false
categories: vim markdown
---

One nice feature that TextMate's Markdown bundle has is being able to easily
mark a header by going to the line after a header, typing # followed by <Tab>,
and having TextMate insert #'s until the last # lines up with the last
character of the title.

```
This Will Be My Header
#<Tab>
```

Turns into this:

```
This Will Be My Header
######################
```
Here's how to do this in Vim:

    :t.|s/./#/g

Don't know what those commands do? Find out with Vim's built-in help (:h, use it!).

In nutshell, `:t.` copies the text of the current line to to the line below
the line given, and then `s/./#/g` substitutes any character on that line with
a '#'.
