---
layout: post.html
title: "errors.js: client side errors object"
date: 2012-03-30 02:05
comments: false
collection:
    - javascript
    - opensource
---

I like ActiveModel's Errors object. It simple, ubiquitous,
consistent, and makes it easy to handle your models' errors, server-side. However, we're deep into the web developers' great migration to the client-side. And developers used to handle errors server-side that they now handle client-side.

[errors.js](http://github.com/travisjeffery/errors.js) is a library I wrote to provide an Errors
object similar to ActiveModel's Errors and provide a simple, consistent interface to handle errors,
client-side.

Here's an end-to-end example showing how it's used:

## Server controller

	class PeopleController < ApplicationController
	  def show
	    @person = Person.find params[:id]
	  end

	  def update
	    @person = Person.find params[:id]
	    @person.update_attributes params[:person]

	    if @person.valid?
	      render :json => @person, :status => 200
	    else
	      render :json => {:errors => @person.errors.full_messages}, :status => 422
	    end
	  end
	end

## Client JavaScript

	jQuery(function($){
	  App = window.App || (window.App = {})

      // configure errors.js to fill in #js-errors with the errors in the response.
	  App.Errors =
	    $("div#js-errors")
	      .errors()
	      .data("errors")

	  $("a.js-person")
	    .on("click", function(event){
	      event.preventDefault()

	      var personId = $("[data-person-id]").data("person-id"),
	      personURL = "/people/" + personId

          // when there's an error response, give the errors to errors.js to update the DOM
	      $.ajax({
	        url: personURL,
	        // => ["Name can't be blank"]
	        data: {id: personId, person: {name: ""}},
	        type: "put",
	        error: App.Errors.handle
	      })
	    })
	})

## View

	<%= link_to @person.name, person_path(@person),
	  :method => "put",
	  :remote => true,
	  :"data-person-id" => @person.id,
	  :class => "js-person"
	%>

	<div id="js-errors"><ul></ul></div>
