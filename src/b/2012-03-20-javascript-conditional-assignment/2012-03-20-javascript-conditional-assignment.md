---
layout: post.html
title: "JavaScript conditional assignment"
date: 2012-03-20 03:18
comments: false
categories: javascript namespaces "conditional assignment"
---

A common idiom with in programming is conditional assignment, usually to
set an undefined variable. Ruby has a nice operator, `||=` for this purpose,
JavaScript doesn't have such an operator. So often variables that are used
across multiple files, like namespaces, have to be repeatedly conditionally
assigned. By not doing so you may try to use the variable before it's been
declared and have a `ReferenceError` thrown.

There
[are](http://stackoverflow.com/questions/881515/javascript-namespace-declaration)
[lots](http://stackoverflow.com/questions/4401323/javascript-best-practice-define-variable-namespace-check-is-not-already-define)
[of](http://blog.arc90.com/2008/06/06/an-easy-way-to-implement-namespaces-in-javascript/)
[ways](http://stackoverflow.com/questions/7639268/nicer-way-of-checking-javascript-namespace) to conditionally assign in JavaScript.
This is the way I learned from Jeremy Ashkenas, and the way I like to do it:

``` js
var Namespace;
Namespace || (Namepace = {});
```

This can also be used for arguments and local variables,

``` js
Namespace.Model = {};

_.extend(Namespace.Model, {
  set: function(attrs, options) {
    options || (options = {});

    if (options.logger) {
      return options.logger.log("Hello. Yes, This is log.")
    }
  }
});

Namespace.Model.set({});
# => ...Nothing/no ReferenceError!

Namespace.Model.set({}, {logger: console})
# => "Hello. Yes, This is log."
```
