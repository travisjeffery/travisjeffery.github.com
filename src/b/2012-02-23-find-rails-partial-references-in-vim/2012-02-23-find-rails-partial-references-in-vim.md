---
layout: post.html
title: "Find rails partial references in vim"
date: 2012-02-23 09:12
comments: false
categories: rails grep vim
published: true
---

Every so often when I'm about to change a partial I need to know how this change
may affect other parts of the application by seeing where and how the partial
is called and used. I've written a Vim command to do this (put in your .vimrc):

``` vim
function! GrepPartial(partial)
  if (a:partial)
    let pattern = "partial.*" . partial
  else
    let path = substitute(expand("%:h"), "app/views/", "", "")
    let action = substitute(expand("%:t:r:r"), "^_", "", "")
    let pattern = "partial.*" . path . "/" . action
  endif

  if (exists('g:loaded_fugitive'))
    execute "Ggrep -P " . '"' . pattern . '\b" app/views'
  elseif (exists('g:ackprg'))
    execute "Ack " . '"' . pattern . '\b" app/views'
  else
    " seriously? use git grep or ack!
    execute "vimgrep " . '"' . pattern . '\>" app/views/*/**'
  endif
endfunction
command! -nargs=? GrepPartial
      \ call GrepPartial(<q-args>)
```

Now while editing a partial just use `:GrepPartial`.

You can also pass in a partial:

`:GrepPartial accounts/show`

Note that if you have Fugitive installed then you'll want to compile git with
the PCRE library, easy for Homebrew users:

`brew install git --with-pcre`

If you don't install PCRE then you'll need to get rid of the `\b`, though your
results may be less accurate.

## Improvements

Right now the function is good-enough for how I use it, though at some point I
may automatically scope partial references when given a non-scoped partial
pattern.

