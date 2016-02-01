var inspect = require('util').inspect

module.exports = plugin;

function plugin() {
  return function (files, metalsmith, done) {
    Object.keys(files).forEach(function (k) {
      console.log('' + k, files[k]);
    })
    done()
  }
}