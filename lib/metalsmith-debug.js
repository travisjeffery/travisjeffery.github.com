var inspect = require('util').inspect

module.exports = plugin;

function plugin() {
  return function (files, metalsmith, done) {
    // console.log(inspect(metalsmith, false, null));
    console.log(metalsmith._metadata.collections.articles);
    // Object.keys(files).forEach(function (k) {
    //   console.log('' + k, files[k]);
    // })
    done()
  }
}