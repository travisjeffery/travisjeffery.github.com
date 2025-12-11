---
title: "Disable microphone muting when typing in Google+ Hangouts"
date: 2013-09-24T00:00:00Z
tags: ["googlechrome"]
aliases:
  - /b/2013/09/disable-microphone-muting-when-typing-in-google-hangouts/
---
In Terminal.app, copy-and-paste and run:

``` sh
defaults write com.google.googletalkplugind exps -string [\"-tm\"]
```
