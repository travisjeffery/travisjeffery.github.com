---
title: "Writing @ prefixed macros"
date: 2014-01-10T00:00:00Z
tags: ["ios"]
---
While writing my own debugging lib, an idea I was toying with was having a debug macro look like one of the built-in @ compiler directives, e.g. @selector, @encode, etc.

Since macro names must be identifiers, and identifiers [can't have @s in them](http://msdn.microsoft.com/en-us/library/e7f8y25b.aspx). You can't do this:

``` objc
#define @debug(fmt, ...) \
  NSLog(fmt, ##__VA_ARGS__)
```

The trick, we'll write our macro such that the macro definition will be missing an @ prefix. When the definition expands, the @ before the real identifier will make our code valid.

``` objc
#define debug(fmt, ...) \
  try {} @finally {} \
  NSLog(fmt, ##__VA_ARGS__)
```

Here, the `try` in the macro is missing its @ prefix. So before and after the preprocessor does its job, we have:

``` objc
// before
@debug(@"My name is Travis.")

// after
@try {} @finally {}
NSLog(@"My name is Travis.");
```

Neat. It's possible you could clash with directives that are added in the future, so namespacing your macros is probably best (e.g. `TRVSDebug`), especially in shared libraries. However, I have seen this techniqued used in [libextobjc](https://github.com/jspahrsummers/libextobjc) — providing macros such as @weakify and @strongify.


