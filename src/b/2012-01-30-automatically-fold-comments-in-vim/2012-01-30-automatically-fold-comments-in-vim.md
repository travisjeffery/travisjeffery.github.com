---
layout: post.html
title: "Comments, and automatically folding them in Vim"
date: 2012-01-17 22:47
comments: false
categories: vim ruby comments documentation automation
---

In general, I tend to side with Robert Martin when it comes to comments, as he puts:

> Nothing can be quite so helpful as a well-placed comment. Nothing can clutter up a module more than frivolous dogmatic comments. Nothing can be quite so damaging as an old crufty comment that propagates lies and misinformation.

> Comments are not like Schindler’s List. They are not “pure good.” Indeed, comments are, at best, a necessary evil. If our programming languages were expressive enough, or if we had the talent to subtly wield those languages to express our intent, we would not need
comments very much—perhaps not at all.

— Robert Martin (Clean Code, p. 53)

Obviously, no matter how expressive you code is, when is comes to public APIs they need to properly documented. Most documentation systems today, such as rdoc; TomDoc; Docco; etc., are implemented such that you need to have many, many lines of comments in your source code. This can cause clutter and difficulty traversing the source code during the times when that's all you care about.

Here's what you can do when editing Ruby with Vim, add this to your .vimrc:

``` vim
autocmd FileType ruby,eruby
      \ set foldmethod=expr |
      \ set foldexpr=getline(v:lnum)=~'^\\s*#'
```

Then when you want to tidy up the comments, fold them away and get out your sight hit `zM`, this will close *all* the folds, your comments, in the file.

Boom! All the comments are neatly tucked away and you can resume programming.

The reason why I don't automatically run the `zM` is because it's possible that Vim may become unresponsive for a short time; each time you open a Ruby file, but you can try for yourself with:

``` vim
autocmd FileType ruby,eruby
      \ set foldmethod=expr |
      \ set foldexpr=getline(v:lnum)=~'^\\s*#' |
      \ exe "normal zM``"
```

For more details on Vim's folding, see the Vim Reference Manual's entry with `:h folding`.
