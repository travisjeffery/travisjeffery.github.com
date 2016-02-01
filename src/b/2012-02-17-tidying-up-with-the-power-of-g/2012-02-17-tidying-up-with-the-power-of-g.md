---
layout: post.html
title: "Tidying up with the power of :g"
date: 2012-02-17 16:37
comments: false
categories: vim
---

Vim's :g takes two inputs, a pattern and an operation, and it runs that operation on
each line that matches the pattern in the current file. :g is a tool whose usage isn't imposed on
you nor even readily apparent, so its usefulness is proportional to your
creativity.

One cool way I like to use :g is to bundle up related lines that are currently
scattered across a file.

Here's an example:

``` vim
Bundle 'git@github.com:travisjeffery/IndexedSearch.git'
" Bundle 'https://github.com/Shougo/neocomplcache.git'
Bundle 'https://github.com/tpope/vim-fugitive.git'
Bundle 'https://github.com/travisjeffery/vim-help'
" Bundle 'https://github.com/Lokaltog/vim-powerline.git'
" Bundle 'https://github.com/jiangmiao/auto-pairs.git'
Bundle 'https://github.com/tpope/vim-ragtag.git'
Bundle 'git@github.com:travisjeffery/vim-rails.git'
" Bundle 'git@github.com:travisjeffery/vim-rails-fork.git'
Bundle 'https://github.com/tpope/vim-repeat.git'
Bundle 'https://github.com/kien/ctrlp.vim.git'
Bundle 'git@github.com:travisjeffery/vim-unimpaired.git'
" Bundle 'https://github.com/thinca/vim-poslist.git'
```

The lines that I care about are the lines that are commented out, in one fell
swoop I'd like to bundle those lines together and put them neatly at the top.
Here's how to do it:

`:g/^"/m 0`

Now our set of lines is nicely bundled together:

``` vim
" Bundle 'https://github.com/thinca/vim-poslist.git'
" Bundle 'git@github.com:travisjeffery/vim-rails-fork.git'
" Bundle 'https://github.com/jiangmiao/auto-pairs.git'
" Bundle 'https://github.com/Lokaltog/vim-powerline.git'
" Bundle 'https://github.com/Shougo/neocomplcache.git'
Bundle 'git@github.com:travisjeffery/IndexedSearch.git'
Bundle 'https://github.com/tpope/vim-fugitive.git'
Bundle 'https://github.com/travisjeffery/vim-help'
Bundle 'https://github.com/tpope/vim-ragtag.git'
Bundle 'git@github.com:travisjeffery/vim-rails.git'
Bundle 'https://github.com/tpope/vim-repeat.git'
Bundle 'https://github.com/kien/ctrlp.vim.git'
Bundle 'git@github.com:travisjeffery/vim-unimpaired.git'
```

:g is one of the most underrated features in Vim, read more about it with `:h :g`.

Here's another way to do the same thing, delete and store the lines into the
register q and the put the contents of the register in line 0:

`:g/^"/d Q`

`:0pu q`

Use lowercase named registers, a-z, to have the register's previous contents replaced
and use uppercase named registers, A-Z, to have the register's previous contents
appended to.

Read more about registers with `:h registers`!
