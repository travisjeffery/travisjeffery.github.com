var moment = require('moment');

module.exports = plugin;

function plugin() {
  return function (files, metalsmith, done) {
    Object.keys(files).forEach(function(k) {
      var f = files[k]
      var d = moment(f.date)
      f.dateShort = d.format('DD-MM-YY')
      f.dateLong = d.format('MM Do, YYYY')
    })
    done()
  }
}