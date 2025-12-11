---
title: "How-to test starting Backbone's history"
date: 2012-04-16T00:00:00Z
tags: ["javascript"]
aliases:
  - /b/2012/04/how-to-test-starting-backbones-history/
---
You can call `Backbone.history.start()` once. Multiple calls
[causes](http://documentcloud.github.com/backbone/docs/backbone.html#section-127) Backbone to throw an Error saying: "Backbone.history has already been started".

You'll hit this error when testing, if you have each test case set up your application, and your application's setup includes starting Backbone:

	App =
	  initialize: (data) ->
	    # ...
	    if not Backbone.history.started?
	      Backbone.history.start({pushState: true})
	      Backbone.history.started = true

You solve this by calling `Backbone.history.stop()` prior to initializing your application:

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
