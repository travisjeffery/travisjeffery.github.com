---
title: "Jasmine-jQuery v2 adding support for Jasmine v2"
date: 2014-01-13T00:00:00Z
tags: [""]
aliases:
  - /b/2014/01/jasmine-jquery-v2-adding-support-for-jasmine-v2/
---
I released Jasmine-jQuery v2.0.0 which adds support for Jasmine v2.0.0.

Jasmine v2 removed support for replacing built-in matchers, which Jasmine-jQuery made use of to replace `toBe()` and `toContain()`, so there are API changes:

- `toBe()` is now `toEqual()`
- `toContain()` is now `toContainElement()`

[Go get it.](https://github.com/velesin/jasmine-jquery/)

Meanwhile, I'll see about patching Jasmine to re-add that feature...
