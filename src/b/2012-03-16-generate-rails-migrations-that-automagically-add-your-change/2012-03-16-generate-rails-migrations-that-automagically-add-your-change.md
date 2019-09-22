---
layout: post.html
title: "Generate Rails migrations that automagically add your change"
date: 2012-03-16 02:56
comments: false
categories: rails migrations generators
---

Rails's generators can be pretty cool, and by knowing some simple tricks
you can save yourself from tedious work:

`rails g model person name:string age:integer`

Rails developers should probably know that this will generate a model
containing name and age fields, with string and integer data types
respectively.

You can even specify attribute options, let's make a new book model with
an indexed price field that needs the given precision 1 and scale 2:

`rails g model book price:decimal{1,2}:index`

This has slightly more magic since it's not apparent what the command does just
by looking at it, e.g. you have to know the precision/scale order.

Things can get even more magical. By naming your migrations in the form of:

`add/remove column [and ...] to/from table`

Rails will generate your migration and add in the change you intend to make.

So let's say we want to add an indexed body and unique person id to the people
table:

`rails g migration add_body_and_pid_to_people body:string:index pid:integer:uniq`

Will generate this migration:

``` ruby
class AddBodyAndPidToPersons < ActiveRecord::Migration
  def change
    add_column :persons, :body, :string
    add_index :persons, :body

    add_column :persons, :pid, :integer
    add_index :persons, :pid, :unique => true
  end
end
```

Pretty cool, huh?

You should always check the generated migration though, it's not perfect.

`rails g migration add_body_to_people body:string:index`

Generates the migration we expect, however,

`rails g migration remove_body_from_people body:string:index`

``` ruby
class RemoveBodyFromPeople < ActiveRecord::Migration
  def up
    remove_column :people, :body
  end

  def down
    add_column :people, :body, :string
  end
end
```

Notice that the specified index will not be added or removed.

Edit: I fixed this issue and it's [merged in Rails](https://github.com/rails/rails/commit/b2a59388b2ad281ccce1f72dd5fda09ca746dc32).
