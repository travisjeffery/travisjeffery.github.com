---
title: "What is this? I don't even... bind this to your object in JavaScript!"
date: 2012-03-29T00:00:00Z
tags: ["javascript"]
---
In JavaScript, the `this` keyword refers to the object it belongs to, and the object depends on where you use it.

- In a method: `this` refers to the owner object.
- In a function: `this` refers to the global object.
- In a function with strict mode: `this` is `undefined`.
- In an event: `this` refers to the element that received the event.
- On its own: `this` refers to the global object.

The way events behave trip up JavaScript developers most. Developers expect `this` to be the global object or the owner of the method handling the event, but `this` refers to the element that received the event. Here's an example:

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

If `this` had referred to the `CarlDouglas` object, then the sing function would have logged
Carl Douglas' "OhohOhoOh... Everybody was Kung fu fighting! Ha!" lyrics. But `this` referred to the element, which has no lyrics.

You can make it so that in your object's method's `this` always refers to the object by using a
technique called binding. You bind your object's methods to that object and ensure that `this`
always refers to object, even when called by an event.

Underscore.js provides the [`bindAll`](http://documentcloud.github.com/underscore/#bindAll) function to bind all of an object's methods to itself. Let's update our previous example to use `bindAll` and see the effect:

    _.bindAll(CarlDouglas)

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


And `this` is `CarlDouglas` as we expected. Everybody was Kung fu fighting! Ha!

![what is this i don't even](http://i0.kym-cdn.com/photos/images/newsfeed/000/228/647/tumblr_ll9huqRApq1qbfddao1_500.jpg)
