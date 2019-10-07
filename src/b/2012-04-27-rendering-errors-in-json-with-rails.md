---
layout: post.html
title: "Rendering errors with JSON and Rails"
date: 2012-04-27 14:58
comments: false
collection: rails
redirectFrom: /b/2012/04/rendering-errors-in-json-with-rails/
---

I've seen bad practices for handling errors with JSON and Rails:

- Not using proper HTTP statuses;
- Not using the error callback; and
- Making errors message building harder than necessary.

Let's look at some examples and how to fix them.

## Not using proper HTTP statuses and the error callback

Callers of your API should know whether their request worked by looking at the response's HTTP status, not by looking at the response's body. When you don't use status codes, every response looks like a successful response:

- Server's controller:

		def create
		  @model = Model.new(params[:model])
		  if @model.save
		    render :json => @model.to_json
		  else
		    render :json => { :errors => @model.errors.full_messages }
		  end
		end

- Client's JavaScript:

		$.ajax(
		  // ...
		    dataType: "json"
		  , success: function(data){
		    if (data.errors) {
		      // do something with errors
		    } else {
		      // do something with successful data
		    }
		  }
		)

Instead, tell your API's caller that their request failed by setting a status code for the error. If the error is the client's fault, use a status code in the 400-499 range; if the error is the server's fault, use a status code in the 500-599 range. [Here's a list of status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status), with information on when to use each.

- Server's controller:

		def create
		  @model = Model.create(params[:model])
		  if @model.save
		    render :json => @model
		  else
		    render :json => { :errors => @model.errors.full_messages }, :status => 422
		  end
		end

- Client's JavaScript:

		$.ajax({
		  // ...
		    dataType: "json"
		  , success: function(data){
		      // do something with successful data
		  }
		  , error: function(xhr){
		      var errors = $.parseJSON(xhr.responseText).errors
		      // do something with errors
		  }
		})

By responding with the 422 status code, your client knows that the response failed. jQuery calls the error callback for you, removing unnecessary logic from your code.

## Making error message building harder than it needs to be

I watched a "Backbone with Rails" screencast where the author had his server respond with `@model.errors`. Then he began to work on his client and he spent 30 minutes working on transforming the `@model.errors` data into the data that `@model.errors.full_messages` would have given him, free.

- `render :json => { :errors => @model.errors }`

    Responds with a object where the keys are your model's attributes with the associated errors:

        { name: ["is blank"], age: ["is not greater than 0"]}

-  `render :json => { :errors => @model.errors.full_messages }`

    Responds with an array of error messages, which you can render straight into a list in the DOM.

        ["Name is blank", "Age is not greater than 0"]
