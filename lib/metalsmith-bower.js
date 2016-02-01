var lib = require('bower-files')();
var read = require('fs').readFileSync;
var basename = require('path').basename;

module.exports = plugin;

function plugin() {
  return function (files, metalsmith, done) {    
    setImmediate(done);
    include(files, 'js', lib.self().ext('js').files)
  }  
}

function include(files, root, included) {
  included.forEach(function(f) {
    var contents = read(f)
    files['' + root + '/' + basename(f)] = { contents: contents };
  })
}