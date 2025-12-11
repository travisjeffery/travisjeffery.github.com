---
title: "Building regexps in JavaScript"
date: 2012-01-05T00:00:00Z
tags: ["javascript"]
aliases:
  - /b/2012/01/building-regexps-in-javascript/
---
If you need to build a JavaScript RegExp from multiple strings or regexps, dynamically, here's how:

``` js
var re = new RegExp("some string" + /some.*(re)/.source);
"some string some        re".match(re);
```

This example shows how to use this technique to parse out information:

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
