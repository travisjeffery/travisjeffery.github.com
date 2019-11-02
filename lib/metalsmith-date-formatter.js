var moment = require('moment');

module.exports = plugin;

function plugin() {
  return function (files, metalsmith, done) {
    Object.keys(files).forEach(function(k) {
      var f = files[k]
      var d = moment(f.date)
      f.year = d.format('YYYY')
      f.month = d.format('MM')
      f.dateShort = d.format('DD/MM/YY')
      f.dateLong = d.format('MMMM Do, YYYY')
    })
    done()
  }
}
