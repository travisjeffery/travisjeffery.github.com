---
layout: post.html
title: "Disable microphone muting when typing in google+ hangouts"
date: 2013-09-24 10:27
comments: true
categories: google google+ hangouts mic microphone config
---

In Terminal.app, copy-and-paste and run:

``` sh
defaults write com.google.googletalkplugind exps -string [\"-tm\"]
```