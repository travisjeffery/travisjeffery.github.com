---
title: "Vim and the power of :g"
date: 2012-02-17T00:00:00Z
tags: ["vim"]
aliases:
  - /b/2012/02/vim-and-the-power-of-g/
---
Vim's `:g` takes two inputs: a pattern and an operation, and it runs that operation on each line
that matches the pattern in the current file. `:g` is a tool whose usage isn't imposed on you, nor
obvious --- its usefulness depends on your creativity.

Here's an example of what `:g` can do: grouping related lines. Take this file:

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

I want the commented lines grouped and moved up top. I run:

    :g/^"/m 0

And `:g` groups the lines. Now this is our file:

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

`:g` is one of the most underrated features in Vim. You can learn more about it by running `:h :g`.
