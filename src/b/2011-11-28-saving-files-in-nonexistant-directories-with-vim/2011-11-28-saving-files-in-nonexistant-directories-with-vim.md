---
layout: post.html
title: "Saving Files in Nonexistent Directories With Vim"
date: 2011-11-28 23:09
comments: false
categories: vim automation
---

Quite often you may find yourself editing a file in a nonexistent directory.

If you're a Rails developer, you may have used:

    :Rview show.html.erb

This creates the show page for the current controller you're working on,
however the app/views/controller directory may not exist yet, and Vim will not
let you save a file in a nonexistent directory. So this what you do:

    :!mkdir %:p:h

`:h expand` to the see the meaning of the modifiers used if you're interested.

An aside, this is what I previously used:


``` vim
augroup vimrc-auto-mkdir
  autocmd!
  autocmd BufWritePre * call s:auto_mkdir(expand('<afile>:p:h'), v:cmdbang)
  function! s:auto_mkdir(dir, force)
    if !isdirectory(a:dir)
          \   && (a:force
          \       || input("'" . a:dir . "' does not exist. Create? [y/N]") =~? '^y\%[es]$')
      call mkdir(iconv(a:dir, &encoding, &termencoding), 'p')
    endif
  endfunction
augroup END
```

This has the benefit of prompting of me when I try to save a file in
non-existent directory. However, I feel like the less configuration I have to
rely on the better, and also, `:!mkdir %:p:%` feels, and looks much more
badass.
