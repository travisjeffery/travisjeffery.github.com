'use strict';

var layouts = require('metalsmith-layouts')
var metalsmith = require('metalsmith')
var browserSync = require('metalsmith-browser-sync')
var branch = require('metalsmith-branch')
var rename = require('metalsmith-rename')
var markdown = require('metalsmith-markdown')
var partials = require('./lib/metalsmith-handlebars-partials')
var sass = require('metalsmith-sass')
var templates = require('metalsmith-templates')
var bower = require('./lib/metalsmith-bower')
var collections = require('metalsmith-collections')
var date = require('./lib/metalsmith-date-formatter')
var permalinks = require('metalsmith-permalinks')
var drafts = require('metalsmith-drafts')
var metallic = require('metalsmith-metallic')
var categories = require('./lib/metalsmith-categories')
var debug = require('./lib/metalsmith-debug')
var redirect = require('metalsmith-redirect')

var pipe = metalsmith(__dirname)
  .source('src')
  .destination('build')
  .use(drafts())
  .use(date({
    dates: [{
      key: 'date',
      format: ''
    }]
  }))
  .use(categories())
  .use(collections({
    medium: {
      pattern: 'm/**/*.md',
      sortBy: 'date',
      reverse: true
    },
    articles: {
      pattern: 'b/**/*.md',
      sortBy: 'date',
      reverse: true
    }
  }))
  .use(partials({
    directory: 'partials'
  }))
  .use(branch('**/*.md')
       .use(metallic())
       .use(markdown({
         smartypants: true,
         gfm: true,
         tables: true
       }))
      )
    .use(branch('**/*.scss')
         .use(sass({
           outputStyle: 'expanded'
         }))
        )
  .use(bower())
  .use(branch('b/**/*')
       .use(permalinks({
         pattern: 'b/:year/:month/:title'
       }))
      )
  .use(redirect({
    '/b/2012/12/overriding-uiviewcontrollers-view-property-done-right': '/b/2012/12/overriding-uiviewcontroller-s-view-property-done-right/'
  }))
  .use(layouts({
    directory: 'layouts',
    engine: 'handlebars',
    pattern: '**/*.html',
    default: 'post.html'
  }));

if (process.env.WATCH) {
  pipe = pipe.use(browserSync({
    server: 'build',
    files : ['src/**/*', 'layouts/**/*', 'partials/**/*']
  }));
}

pipe.build(function(err) {
  if (err) throw err
});