---
layout: post.html
title: "How-to test starting backbone's history"
date: 2012-04-16 03:32
comments: false
categories: backbone backbonejs history start testing
---

`Backbone.history.start()` can be only be called once, doing otherwise will
[cause](http://documentcloud.github.com/backbone/docs/backbone.html#section-127) an Error to be thrown with the message "Backbone.history has already been started".

This can be annoying when testing because it's common practice to have an App
namespace that contains a initializer method to setup your application,
including starting Backbone's history.

``` coffeescript
App =
  initialize: (data) ->
    # ...
    if not Backbone.history.started?
      Backbone.history.start({pushState: true})
      Backbone.history.started = true
```

But each test case you write that calls this initializer method will also call
`Backbone.history.start()`. The solution is use `Backbone.history.stop()` which
will disable history temporarily.

``` coffeescript
describe "App", ->
  describe "#initialize", ->
    it "starts Backbone.history", ->
      Backbone.history.started = null
      Backbone.history.stop()
      sinon.spy(Backbone.history, "start")
      App.initialize {}

      expect(Backbone.history.start).toHaveBeenCalled()

      Backbone.history.start.restore()
```

## Source

[Addition of Backbone.history.stop()](https://github.com/documentcloud/backbone/pull/538)
