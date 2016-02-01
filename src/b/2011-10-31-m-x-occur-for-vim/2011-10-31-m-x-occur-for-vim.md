---
layout: post.html
title: "M-x occur for vim"
date: 2011-10-31 02:11
comments: false
categories: vim emacs grep
---

Emacs has a pretty great feature called "Occur" and to use it you do the ol'
M-x occur. But I'm a Vim user, and so this is the solution I've come up with:

<pre><code>nmap g/ :vimgrep /&lt;C-R&gt;//j %&lt;CR&gt;\|:cw&lt;CR&gt;</code></pre>

So my work flow is as follows:

1. I search for what I'm trying to find with the usual `/my query<CR>`.

2. If I didn't hit what I was looking for then I hit `g/` and find the line
   containing what I'm looking for and hit <CR> to be taken there.

If this isn't your work flow, you could create a function that takes your query
as input and uses that as your pattern instead of what you last searched for
(the `<C-R>/` part). Or if you're not a fan of the QuickFix buffer, what I
previously used was `nmap g/ global//print`, but I feel what I have now is
superior.

