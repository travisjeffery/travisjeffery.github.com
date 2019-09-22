---
layout: post.html
title: "What is this? I don't even... bind this to your object in JavaScript!"
date: 2012-03-29 01:08
comments: false
categories: scope this javascript bind trigger events context
---

In JavaScript, a function's `this` keyword is always bound to an object, what
object that is depends on how the current function was called, so it could be
different each time the function is called.

In this example, as we and anyone else would expect after reading this code,
`this` refers to MyObject,

``` js
var MyObject = {
  my_method: function(){
    console.log(this)
  },

  inspect: function(){
    return "I'm MyObject!"
  }
}

MyObject.my_method()

// > I'm MyObject!
```

The next example is a little weird. As you can see my_method is now being
called within the context of the global object.

In the previous case my `console.log(this)` was equivalent to
`console.log(MyObject)` and here it is equivalent to `console.log(global)`.

``` js
var MyObject = {
  // ...
}

global.inspect = function(){
  return "I'm the Global Object!"
}

var my_same_method = MyObject.my_method
my_same_method()

// > I'm the Global Object!
```

But the really interesting stuff happens when using something like jQuery's
Events with `bind/trigger`. I've seen this be a fairly common gotcha. You
expect `this` to refer to your object, but it's actually the object you
triggered your event on,

``` js
var myDiv = $("body").append("<div id='js-my-div'></div>")

var CarlDouglas = {
  lyrics: "OhohOhoOh... Everybody was Kung fu fighting! Ha!",

  sing: function(){
    this.lyrics || (this.lyrics = "Where are Carl Douglas's lyrics?! What this is _this_??")

    console.log(this.lyrics)
  }
}

myDiv.bind("kungfu:fight", CarlDouglas.sing)

$("div#js-my-div").trigger("kungfu:fight")

// > Where are Carl Douglas's lyrics?! What this is _this_??
```

Thankfully, this is fixable! All we have to do in bind our object's methods to
that object, to be run in the context of our object whenever they are invoked.

Underscore.js provides this functionality with its `bind/bindAll` functions, check out
the [docs](http://documentcloud.github.com/underscore/#bind) and [annotated
sources](http://documentcloud.github.com/underscore/docs/underscore.html#section-52) for more detail.

So we add this after defining our object,

``` js
_.bindAll(CarlDouglas)
```

And `this` behaves as we expect! Everybody was Kung fu fighting! Ha!

``` js
var myDiv = $("body").append("<div id='js-my-div'></div>")

var CarlDouglas = {
  lyrics: "OhohOhoOh... Everybody was Kung fu fighting! Ha!",

  sing: function(){
    this.lyrics || (this.lyrics = "Where are Carl Douglas's lyrics?! What this is _this_??")

    console.log(this.lyrics)
  }
}

_.bindAll(CarlDouglas)

myDiv.bind("kungfu:fight", CarlDouglas.sing)

$("div#js-my-div").trigger("kungfu:fight")

// > OhohOhoOh... Everybody was Kung fu fighting! Ha!
```

![what is this i don't even](http://i0.kym-cdn.com/photos/images/newsfeed/000/228/647/tumblr_ll9huqRApq1qbfddao1_500.jpg)
