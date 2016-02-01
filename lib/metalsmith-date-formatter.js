var moment = require('moment');

module.exports = plugin;

function plugin() {
  return function (files, metalsmith, done) {
    Object.keys(files).forEach(function(k) {
      var f = files[k]
      var d = moment(f.date)
      f.shortDate = d.format('DD-MM-YY')
      f.longDate = d.format('MM Do, YYYY')
    })
    done()
  }
}