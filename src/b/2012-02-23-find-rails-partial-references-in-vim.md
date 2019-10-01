---
layout: post.html
title: "Find Rails partial references in Vim"
date: 2012-02-23 09:12
comments: false
collection:
    - vim
    - rails
published: true
---

Before I change a Rails partial that's shared across the project, I check what effect my change will have by looking at where and how the partial's used. In Vim, I find the references to  partials with the following function:

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

Here's how the command works:

- `:GrepPartial` finds references to the current partial you're editing.
- `:GrepPartial accounts/show` find references to the accounts/show partial.

The function uses Fugitive if you have it installed, and if you do then you'll want to install git with the PCRE library. Homebrew users can install git with PCRE by running:

    brew install git --with-pcre
