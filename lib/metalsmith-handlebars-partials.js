var basename = require('path').basename;
var extname = require('path').extname;
var handlebars = require('handlebars');

module.exports = plugin;

function plugin() {
  var dir = 'partials';
      
  return function(files, metalsmith, done) {      
    setImmediate(done);
      
    Object.keys(files).forEach(function(file) {
      if (file.indexOf(dir + '/') !== 0) return;
      var data = files[file];
      var name = basename(file, extname(file));
      var str = data.contents.toString();
      handlebars.registerPartial(name, str);
      delete files[file];
    })
  }
}