---
layout: post.html
title: "Error Responses on Node.js with Koa"
date: 2015-10-21 02:08
comments: false
published: true
categories: node koa errors
---

Koa is a web framework that's the next generation Express in that it's built by
the same team, and aims to be smaller, more expressive, and more robust for
building web applications and APIs. It accomplishes this in large part by
using generators which enables writing asynchronous JS without callbacks and
greatly simplifies flow control and handling errors.

In this article I'm gonna show how you can use Koa to simplify sending error
responses. If you get lost with the
terminology here I recommend skimming over the Koa [docs](http://koajs.com/) or
[asking me a question](https://twitter.com/travisjeffery).

A Koa application is an object containing an array of middleware generator
functions that are composed and ran in a stack-like manner upon request. The
most basic error response middleware would look something like this:

``` js
app.use(function *(next) {
  try {
    // yield downstream
    yield next;
  } catch (err) {
    this.status = err.status || 500;
    this.body = err.message;
  }
});
```

Somewhere downstream you'd have a call to a generator like `findByEmail` below that would
throw. For example, we're throwing an error here when the given user isn't found.

``` js
Users.prototype.findByEmail = function*(email) {
  let user = yield this.db.findOne({ email: email });
  if (!user) {
    let err = new Error('User not found');
    err.status = 404;
    err.message = `User not found with email: ${email}`;
    throw err;
  }
  return user;
}
```

With this implementation, you'd have to do something similar for each of your
APIs and error responses. E.g. 401 for when the user isn't logged-in, 403 for
bad attributes, etc.

Let's find another way to have a well contained and clean way to send back those
error responses and even share those responses between code bases with different
languages.

First we put our error response schema in YAML. This makes for a very clean and
nicely structured schema, and also means that you could use the same error
schema in another language.

``` yaml
user_not_found:
  message: User not found with ":email"
  status: 404
```

Our `findByEmail` implementation looks like this now:

``` js
Users.prototype.findByEmail = function*(email) {
  let query = { email: email };
  let user = yield this.db.findOne(query);
  if (!user) {
    this.thrower.throw('user_not_found', query);
  }
  return user;
}
```

Here's `thrower.throw`, which is used to add the key/values from `extra` onto
the error which will then be used to fill in the user's email into the error
message.

``` js
Thrower.prototype.throw = function(msg, extra) {
  let err = new Error(msg);
  for (let k in extra) {
    err[k] = extra[k];
  }
  throw err;
}
```

And for our error middleware we have:

``` js
let fmt = require('format-string');

app.use(function *(next) {
  try {
    yield next;
  } catch (err) {
    let schema = schemas[err.message];
    if (schema) {
      this.status = schema.status;
      this.body = fmt(schema.message, err);
    } else {
      this.status = err.status || 500;
      this.body = err.message;
    }
  }
});
```

And voila you have a scalable and simple system for sending back error responses.

This is also makes adding error tracking very easy too, since you have a single
point of contact where all errors with go through. So you can make a single call
to Sentry, or some other JS error tracker here.

``` js
let fmt = require('format-string');

app.use(function *(next) {
  try {
    yield next;
  } catch (err) {
    let schema = schemas[err.message];
    this.errorTracker.track(err); // Send error to sentry or wherever
    if (schema) {
      this.status = schema.status;
      this.body = fmt(schema.message, err);
    } else {
      this.status = err.status || 500;
      this.body = err.message;
    }
  }
});
```

I'll be open sourcing a lib to help bootstrap this setup shortly.
