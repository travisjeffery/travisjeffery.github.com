---
layout: post.html
title: "Building regexps in JavaScript"
date: 2012-01-05 22:43
comments: false
collection: javascript
---

Let's say you want to put together a JavaScript RegExp wherein you want, or
need, to put together multiple strings or regexps then here's the short version
to get you on your way:

``` js
var re = new RegExp("some string" + /some.*(re)/.source);
"some string some        re".match(re);
```

Here's a longer example showing a more in-depth and possibly practical example:

In this example let's say you have something like an HTML table whose rows
contain some information that you need to parse out, like ids,


``` js
var _ = require('underscore');

function Table(rows, options){
    if (!(this instanceof Table)){
        return new Table(rows, options);
    }

    var self = this;

    self.rows = rows;
    self.options = options;

    self._id_for_row = function(row){
        var re = new RegExp(self.options.field_name + /_(\d+)/.source);
        return row.match(re)[1];
    }

    self.row_ids = function(){
        return _.map(self.rows, self._id_for_row);
    };
}

var table = new Table(
    ["user_name_field_1", "user_name_field_22", "user_name_field_23"],
    {"field_name":"user_name_field"}
);

###
#
# > console.log(table.row_ids());
# => [ '1', '22', '23' ]
```
