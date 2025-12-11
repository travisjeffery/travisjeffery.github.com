---
title: "Using PostgreSQL's Hstore with Rails"
date: 2012-02-20T00:00:00Z
tags: ["postgres"]
aliases:
  - /b/2012/02/using-postgresqls-hstore-with-rails/
---
## Prelude

Recently I implemented a piece of functionality that used PostgreSQL's hstore
data type in a Rails application and I'd like to share how we did it including
some improvements you can make to use data stored as an hstore easier.

hstore is PostgreSQL data type similar to integer, date and text, but
unlike these atomic data types hstore stores key/value pairs within a single
PostgreSQL value.

Hashes/dictionaries are the most used data structure in computer science and
programming so having them as a data type in a database is massively
powerful with many use cases, e.g. dynamic columns.

Rails can actually already do this by adding a text field to a table and
calling serialize like so:

``` ruby
class MyModel < ActiveRecord::Base
  serialize :field, Hash
end
```

The problem with this is that a field stored and serialized in this manner will not
support indexing and lookups will be very slow. hstore on the other hand does support indexing.

![Graph](https://docs.google.com/spreadsheet/oimg?key=0At-PylhYQ8Q0dDVlblluWW1kQUxpZWUyZElLMVJCUmc&oid=1&zx=jfvyr8xso2hq)

## Using hstore with rails today

Any Rails version < v4.0/master does not support hstore out of
the box. Thankfully there's a gem: [activerecord-postgres-hstore](https://github.com/softa/activerecord-postgres-hstore)
that provides support. See the project's README on GitHub for installation
instructions.

## Usage

### Creating an entity

I'm going to create a person model that has a preferences field stored as an
hstore.

`rails g model Person name:string preferences:hstore`

`rake db:migrate`

`CREATE INDEX people_gin_preferences ON people USING GIN(preferences);`

### Storage and retrieval

Now we have our Person entity and we can use it with `@travis.preferences["key"]` like so, serialization/deserialization is handled
for us:

``` ruby
require 'test_helper'

class PersonTest < ActiveSupport::TestCase
  def setup
    @travis = Person.create :name => "Travis Jeffery", :preferences => {"private?" => true, "location" => "Toronto, Ontario"}
  end

  test "accessing preferences" do
    assert_equal true, @travis.preferences["private?"]
    assert_equal "Toronto, Ontario", @travis.preferences["location"]
  end
end
```

## Improving the api

This API is not very nice and has bad encapsulation, how much cooler would
it be to be able to just use `@travis.private?` or `@travis.location`? Here's
how:

``` ruby
class Person < ActiveRecord::Base
  def method_missing(id, *args, &block)
    if preferences.has_key?(id.to_s)
      preferences.fetch(id.to_s)
    else
      super
    end
  end
end
```

## Issues

`PG::Error: ERROR:  type "hstore" does not exist`

## Schema load/dump

One problem you may run into is when you try to `rake db:test:prepare` is that
Rails will not be able to load the schema properly since it doesn't support
hstore yet, to fix this you can either dump to sql by uncommenting or adding to your
application configuration in config/application.rb:

`config.active_record.schema_format = :sql`

Or make similar [changes](https://github.com/rails/rails/pull/4896) to what's
in master right now in a config/initializer or something and then delete
that initializer when you upgrade to 4.0.

## Add hstore to your template database

Another issue is that when you ran the migration to create the hstore data type to
your database, it was only added to the database for your current environment.

This will be okay for development and production, but if you drop your test
database and create it again you won't have the hstore data type, so to fix this
create the hstore data type on your template1 database:

`psql -f PATH/hstore.sql -d template1`

You can find this hstore.sql find usually within PostgreSQL's contrib folder on
your system.

## Using hstore with rails in the future

Full support for hstore is in Rails master and will likely be in Rails v4.0. So
if you're on master you shouldn't don't need to worry about any these issues other than making sure your
database does actually have the hstore data type. I would recommend improving the API and encapsulation as I've done above too.

It's an exciting time to be PostgreSQL and Rails developer!

## Further reading:

- PostgreSQL's [reference documentation](http://www.postgresql.org/docs/9.1/static/hstore.html) on hstore
- More on PostgreSQL's template databases and how creating a database in
PostgreSQL works [here](http://www.postgresql.org/docs/8.1/static/manage-ag-templatedbs.html).
