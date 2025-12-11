---
title: "JavaScript conditional assignment"
date: 2012-03-20T00:00:00Z
tags: ["javascript"]
aliases:
  - /b/2012/03/javascript-conditional-assignment/
---
Ruby has a conditional assignment operator: `||=`.
JavaScript doesn't have such an operator. Common use cases for conditional assignment that JavaScript developers use are lazily defining a namespace and defaulting function arguments.

Since JavaScript has no built in conditional assignment operator, the language leaves conditional assignment as a stylistic choice for JavaScript developers. The following is the style I like, which I learned from Jeremy Ashkenas.

- Defining a namespace:

	    var Namespace;
	    Namespace || (Namepace = {});

- Function arguments:

        Namespace.Model = {};

		_.extend(Namespace.Model, {
		  set: function(attrs, options) {
		    options || (options = {});

		    if (options.logger) {
		      return options.logger.log("Hello. Yes, This is log.")
		    }
		  }
		});
