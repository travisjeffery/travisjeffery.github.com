---
layout: post.html
title: "Comments, and automatically folding them in Vim"
date: 2012-01-17 22:47
comments: false
collection: vim
---

No matter how clean your code is, you need to document your code.

> Nothing can be quite so helpful as a well-placed comment. Nothing can clutter up a module more than frivolous dogmatic comments. Nothing can be quite so damaging as an old crufty comment that propagates lies and misinformation.

> Comments are not like Schindler’s List. They are not “pure good.” Indeed, comments are, at best, a necessary evil. If our programming languages were expressive enough, or if we had the talent to subtly wield those languages to express our intent, we would not need
comments very much—perhaps not at all.

— Robert Martin (Clean Code, p. 53)

However, when you're focused on coding a feature in a code base that you know well then the comments
can get in your way. Most documentation systems today --- rdoc, TomDoc, Docco, and so forth ---
require many lines of comments and slow down how fast you can move through the code. Sometimes it's nice to hide the comments.

Vim has a folding feature that you can use to temporarily hide comments. This configuration tells Vim how to fold Ruby comments:

``` vim
autocmd FileType ruby,eruby
      \ set foldmethod=expr |
      \ set foldexpr=getline(v:lnum)=~'^\\s*#'
```

There's a handful of folding keybinds, the binds I use in order of most-to-least often:

- `zM`: close all folds in the current file;
- `zR`: open all folds in the current file;
- `zc`: close the fold under the cursor;
- `zo`: open the fold under the cursor.

Read Vim's reference manual by running `:h folding` for the complete documentation.
