---
layout: post.html
title: "Expressive domain specific languages (DSL) in Ruby"
date: 2011-12-28 23:21
comments: false
collection: ruby
---

I've experimented with making DSLs in Ruby and here's an example:

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

---

> u = User.new do
  name       "Travis Jeffery"
  location   "Toronto, Ontario"
  occupation "Mathematician, Software Engineer"
end
> u.name
=> "Travis Jeffery"
> u.location
=> "Toronto, Ontario"
> u.occupation
=> "Mathematician, Software Engineer"
```

By checking the arity of the block, we support this API too:

``` ruby
u = User.new do |u|
  u.name "Travis Jeffery"
end
```

I prefer the first example but I wouldn't use either in a real project. But the idea could be useful for something useful.
