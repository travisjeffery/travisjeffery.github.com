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

metalsmith(__dirname)
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
        pattern: 'b/:year/:month/:title',
        date: 'YYYY/MM'  
      }))  
    )
  .use(layouts({
    directory: 'layouts',
    engine: 'handlebars',
    pattern: '**/*.html',
    default: 'post.html'
  }))
  .use(browserSync({
    server: 'build',
    files : ['src/**/*', 'layouts/**/*', 'partials/**/*']
  }))
  .build(function(err) {
    if (err) throw err
  });