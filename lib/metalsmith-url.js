'use strict';

var _ = require('lodash');

module.exports = function(url) {
  return function(files, metalsmith, done) {
    _.each(files, function(file){
      file.url = url;
    });
    done();
  };
}
