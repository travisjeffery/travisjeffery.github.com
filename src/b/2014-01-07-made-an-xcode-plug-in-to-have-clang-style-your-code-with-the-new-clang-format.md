---
layout: post.html
title: "My Xcode plug-in to have Clang format/style your code using the new clang-format"
date: 2014-01-07 09:50
comments: true
collection:
    - ios
    - xcode
---

Recently added to Clang v3.4 are [awesome tools for formatting your code](http://clang.llvm.org/docs/ClangFormat.html) and a new command `clang-format`.

Clang format can style code to guidelines of LLVM, WebKit, Google, Chromium, Mozilla, or you can create your own configurations.

[I wrote an Xcode plug-in to use clang-format from within Xcode](https://github.com/travisjeffery/ClangFormat-Xcode):

![demo](https://raw.github.com/travisjeffery/ClangFormat-Xcode/master/README/clangformat-xcode-demo.gif)

Pretty neat.

This was my first Xcode plug-in so that was pretty interesting and I learned a lot about Cocoa plug-ins, how Xcode's implementation works, and some generally useful tricks for replacing ranges in text views and how to replace a selected range with a string of a different size and refit the selection for the inserted text.
