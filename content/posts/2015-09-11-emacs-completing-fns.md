---
title: "Writing your own Emacs interactive functions with completion"
date: 2015-09-11T00:00:00Z
aliases:
  - /b/2015/09/writing-your-own-emacs-interactive-functions-with-completion/
---
Here's how to use [Ido](http://emacswiki.org/emacs/InteractivelyDoThings) in Emacs to write your own interactive functions with completion. In this example, we'll make a function that completes directories but Ido provides functions for reading files, buffers, and more.

This function will go to the given repo in my dev directory, and if that repo isn't cloned yet, will clone it from my GitHub first.

``` scheme
(defun tj-goto (repo)
  "Go to or clone the given dev `repo'."
  (interactive
   (list
    (ido-read-directory-name "Directory: " "~/dev/")))
  (let* ((dev-dir "~/dev/")
         (repo-dir repo))
    (if (file-exists-p repo-dir)
        (projectile-find-file-in-directory repo)
      (shell-command (format "cd %s; git clone git@github.com:travisjeffery/%s.git" dev-dir repo))
      (projectile-find-file-in-directory repo))))
```
