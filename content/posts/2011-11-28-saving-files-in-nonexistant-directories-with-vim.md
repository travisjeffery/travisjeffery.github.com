---
title: "Saving files in nonexistent directories with Vim"
date: 2011-11-28T00:00:00Z
tags: ["vim"]
aliases:
  - /b/2011/11/saving-files-in-nonexistent-directories-with-vim/
---
I often open a file in a directory that doesn't exist yet. However, Vim will not let you save a file
in a nonexistent directory.

You can manually create the directory by running the following command:

```
:!mkdir %:p:h
```

You can automate creating the directory with the following autocommand:

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

With this command, when you save a file in nonexistent directory, Vim will ask you if you want the directory created and then create it.
