---
layout: post.html
title: "Tidying up with the power of :g"
date: 2012-02-17 16:37
comments: false
collection: vim
---

Vim's :g takes two inputs: a pattern and an operation, and it runs that operation on
each line that matches the pattern in the current file. :g is a tool whose usage isn't imposed on
you, nor even readily apparent, so its usefulness depends on your
creativity.

For example, I like to use :g to group related lines that are currently
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

The lines that I care about are the commented out lines. In one fell swoop I can group those lines
and put them at the top by running the following:

```
:g/^"/m 0
```

The result with our lines grouped together:

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

:g is one of the most underrated features in Vim. You can read more about it by running `:h :g`.
