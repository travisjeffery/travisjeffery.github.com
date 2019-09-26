---
layout: post.html
title: "Disable microphone muting when typing in Google+ Hangouts"
date: 2013-09-24 10:27
comments: true
collection: googlechrome
---

In Terminal.app, copy-and-paste and run:

``` sh
defaults write com.google.googletalkplugind exps -string [\"-tm\"]
```
