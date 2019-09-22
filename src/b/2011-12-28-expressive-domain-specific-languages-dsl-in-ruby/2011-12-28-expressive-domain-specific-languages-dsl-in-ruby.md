---
layout: post.html
title: "Expressive domain specific languages (DSL) in Ruby"
date: 2011-12-28 23:21
comments: false
categories: ruby domain-specific-languages dsl
---

In this example, I'm creating a User object such that I can set the name using
my own DSL:

``` ruby
class User
  def initialize &block
    if block.arity == 1
      block[self]
    else
      instance_eval &block
    end
  end

  def name new_name = nil
    @name ||= new_name
  end

  def location new_location = nil
    @location ||= new_location
  end

  def occupation new_occupation = nil
    @occupation ||= new_occupation
  end
end

u = User.new do
  name       "Travis Jeffery"
  location   "Toronto, Ontario"
  occupation "Mathematician, Software Engineer"
end

###
#
# > u.name
# => "Travis Jeffery"
# > u.location
# => "Toronto, Ontario"
# > u.occupation
# => "Mathematician, Software Engineer"
```

The reason for checking the arity of the block given is so you can support the case when a user of our API would use it like so:

``` ruby
u = User.new do |u|
  u.name "Travis Jeffery"
end
```

Personally, I'd be inclined to support only one interface—my preference being the first one.
