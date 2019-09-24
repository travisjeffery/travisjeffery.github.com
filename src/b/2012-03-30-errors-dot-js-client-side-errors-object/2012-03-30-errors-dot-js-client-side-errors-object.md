---
layout: post.html
title: "errors.js: client side errors object"
date: 2012-03-30 02:05
comments: false
collection:
    - javascript
    - opensource
---

Despite my opinions of ActiveModel::Validations (a post/patch for another day),
I like ActiveModel's Errors object. Errors's simplicity, ubiquity, and
consistency is a great boon for handling error messages of varying entities.

The future of the web is asynchronous and client side computation is steadily becoming more
sophisticated and well practiced.

errors.js provides an Errors object similar to ActiveModel's Errors object to
provide a simple, ubiquitous, consistent interface to handle and use error
messages on the client side.

[errors.js is on GitHub](http://github.com/travisjeffery/errors.js), here is the source,

``` js
(function($, _){
  $.widget("travisjeffery.errors", {
    _create: function(){
      _.bindAll(this)
      this.container = this.element
      this.list = this.element.find("ul")
    }
  })

  $.extend($.travisjeffery.errors.prototype, {
    add: function(error){
      var errors = this._buildErrorList(error)

      this.reset()
      this.show()

      this.list.append(errors)
    },

    show: function(){
      this.container.show()
    },

    hide: function(){
      this.container.hide()
    },

    reset: function(){
      this.hide()
      this.list.empty()
    },

    handle: function(xhr, status, error){
      var errors = $.parseJSON(xhr.responseText).errors
      this.add(errors)
    },

    _buildErrorList: function(errors){
      var errorArray = $.makeArray(errors),
      stringToItem = function(message){return "<li>"+ message +"</li>"},
      errorList = $.map(errorArray, stringToItem).join("\n")

      return errorList
    }
  })
}(jQuery, _));
```


It's small and really simple, and only depends on jQuery/UI and Underscorejs. Using it looks
like this,

## Controller

```ruby
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
```

## Javascript asset

``` js
jQuery(function($){
  App = window.App || (window.App = {})
  App.Errors =
    $("div#js-errors")
      .errors()
      .data("errors")

  $("a.js-person")
    .on("click", function(event){
      event.preventDefault()

      var personId = $("[data-person-id]").data("person-id"),
      personURL = "/people/" + personId

      $.ajax({
        url: personURL,
        // => ["Name can't be blank"]
        data: {id: personId, person: {name: ""}},
        type: "put",
        error: App.Errors.handle
      })
    })
})
```

## View

``` erb
<%= link_to @person.name, person_path(@person),
  :method => "put",
  :remote => true,
  :"data-person-id" => @person.id,
  :class => "js-person"
%>

<div id="js-errors"><ul></ul></div>
```

## Api (usable without #handle callback)

``` js
var Errors = $("div#errors").errors().data("errors")

Errors.add("You shall not pass!")

Errors.show()

Errors.hide()

Errors.reset()
```
