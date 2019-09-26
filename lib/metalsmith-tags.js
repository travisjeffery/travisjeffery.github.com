'use strict';

var _ = require('lodash');

module.exports = function() {
  return function(files, metalsmith, done) {
    _.each(files, function(file){
      if (!file.collection) {
        file.tagsString = ''
      }
      file.tagsString = _.without(file.collection, 'articles', 'recent').join(', ')
    });
    done();
  };
}
