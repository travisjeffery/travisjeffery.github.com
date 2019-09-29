---
layout: post.html
title: "Markdown headers in Vim"
date: 2011-11-18 02:06
comments: false
collection: vim
---

With TextMate's Markdown bundle, you can mark headers by moving your cursor to the line
after the intended header, typing `#` and pressing `<Tab>`. The Textmate bundle insert #'s until the
last # aligns with the header's last character.

For example:

```
This Will Be My Header
#<Tab>
```

Turns into:

```
This Will Be My Header
######################
```

Here's the equivalent feature in Vim:

```
:t.|s/./#/g
```

`:t.` copies the current line to the next line and `s/./#/g` substitutes any character on that line with a #. Use Vim's built-in help command, e.g. `:h :t`, for more details.
