'use strict';

var _ = require('lodash');

module.exports = function() {
  return function(files, metalsmith, done) {
    _.each(files, function(file){
      if (!file.categories) return;
      file.categories = file.categories.split(' ').join(', ')
    });
    done();
  };
}