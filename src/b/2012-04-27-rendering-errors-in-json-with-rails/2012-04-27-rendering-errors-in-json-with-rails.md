---
layout: post.html
title: "Rendering errors in JSON with Rails"
date: 2012-04-27 14:58
comments: false
collection: rails
---

Having seen a lot of bad practices when it comes to handling and rendering
errors in JSON, bad practices such as misusing HTTP statuses, success/error
callbacks, and making building error messages harder than necessary, here are
bad and good practices.

Here's an example that is bad,

JavaScript,

``` js
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
```

Controller,

``` ruby
def create
  @model = Model.new(params[:model])
  if @model.save
    render :json => @model.to_json
  else
    render :json => { :errors => @model.errors.full_messages }
  end
end
```

The biggest concern in the example above is that we're not using HTTP statuses
as they were intended which is bad both practically and semantically.

Semantically in the sense that with this implementation we have to mix error
handling in a success callback. Practically since our browser and libraries can
work together to extract the switch logic.

This is a good example,

JavaScript,

``` js
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
```

Controller:

``` ruby
def create
  @model = Model.create(params[:model])
  if @model.save
    render :json => @model
  else
    render :json => { :errors => @model.errors.full_messages }, :status => 422
  end
end
```

With an HTTP error status (e.g. 422 unprocessable entity) our error callback
is called for us, our code is more declarative and without unnecessary logic.

Another small nit-pick is that we're now letting Rails serialize our data according
to our response type, i.e. it will call to\_json for us.

Another tip is to use full\_messages rather than serializing the errors object
as it is,

``` ruby
render :json => { :errors => @model.errors }
```

The above will present the errors in a hash where the keys are attributes and the
values are errors,

``` ruby
# => { name: ["is blank"], age: ["is not greater than 0"]}
```

``` ruby
render :json => { :errors => @model.errors.full_messages }
```


full\_messages on the other hand will return an array of full messages,

``` ruby
# => ["Name is blank", "Age is not greater than 0"]
```

I once watched a Rails/Backbone screencast where the author serialized the
errors object as is and spent ~30 mins manipulating the data client-side into exactly what
full\_messages returned.

This is much easier to work with and I have never once needed the data given by
serializing model.errors.
