'use strict';

var layouts = require('metalsmith-layouts')
var metalsmith = require('metalsmith')
var browserSync = require('metalsmith-browser-sync')
var branch = require('metalsmith-branch')
var rename = require('metalsmith-rename')
var markdown = require('metalsmith-markdown')
var partials = require('./lib/metalsmith-handlebars-partials')
var sass = require('metalsmith-sass')
var bower = require('./lib/metalsmith-bower')
var collections = require('metalsmith-collections')
var date = require('./lib/metalsmith-date-formatter')
var permalinks = require('metalsmith-permalinks')
var drafts = require('metalsmith-drafts')
var metallic = require('metalsmith-metallic')
var debug = require('./lib/metalsmith-debug')
var redirect = require('metalsmith-redirect')
var feed = require('metalsmith-feed')
var tags = require('./lib/metalsmith-tags')
var excerpt = require('metalsmith-excerpts')

var colors = {
  calls: 0,
  colors: ['pink', 'lightcyan', 'lightgreen', 'yellow', 'peachpuff', 'aquamarine', 'paleturquoise', 'lavender', 'coral'],
  next: function() {
    return this.colors[this.calls++%this.colors.length]
  }
}

var url = process.env.URL || 'https://travisjeffery.com'

var pipe = metalsmith(__dirname)
    .metadata({
      site: {
        title: 'travis jeffery',
        url: url,
        author: 'Travis Jeffery'
      }
    })
    .source('src')
    .destination('build')
    .use(drafts())
    .use(date({
      dates: [{
        key: 'date',
        format: ''
      }]
    }))
    .use(collections({
      articles: {
        pattern: 'b/**/*.md',
        sortBy: 'date',
        reverse: true,
        metadata: {
          homepage: false,
        }
      },
      recent: {
        pattern: 'b/**/*.md',
        sortBy: 'date',
        reverse: true,
        limit: 10,
        metadata: {
          name: 'most recent posts',
          recent: true,
          homepage: true,
          color: colors.next(),
        }
      },
      engineering: {
        sortBy: 'date',
        reverse: true,
        metadata: {
          name: 'engineering',
          homepage: true,
          color: colors.next(),
        }
      },
      communication: {
        sortBy: 'date',
        reverse: true,
        metadata: {
          name: 'communication',
          homepage: true,
          color: colors.next(),
        }
      },
      kafka: {
        sortBy: 'date',
        reverse: true,
        metadata: {
          name: 'kafka',
          homepage: true,
          color: colors.next(),
        }
      },
      ops: {
        sortBy: 'date',
        reverse: true,
        metadata: {
          name: 'ops',
          homepage: true,
          color: colors.next(),
        }
      },
      opensource: {
        sortBy: 'date',
        reverse: true,
        metadata: {
          name: 'open source',
          homepage: true,
          color: colors.next(),
        }
      },
      go: {
        sortBy: 'date',
        reverse: true,
        metadata: {
          name: 'go',
          homepage: true,
          color: colors.next(),
        }
      },
      vim: {
        sortBy: 'date',
        reverse: true,
        metadata: {
          name: 'vim',
          homepage: true,
          color: colors.next(),
        }
      },
      javascript: {
        sortBy: 'date',
        reverse: true,
        metadata: {
          name: 'javascript',
          homepage: true,
          color: colors.next(),
        }
      },
      git: {
        sortBy: 'date',
        reverse: true,
        metadata: {
          name: 'git',
          homepage: true,
          color: colors.next(),
        }
      },
      tools: {
        sortBy: 'date',
        reverse: true,
        metadata: {
          name: 'tools',
          homepage: true,
          color: colors.next(),
        }
      },
      rails: {
        sortBy: 'date',
        reverse: true,
        metadata: {
          name: 'rails',
          homepage: true,
          color: colors.next(),
        }
      },
      ruby: {
        sortBy: 'date',
        reverse: true,
        metadata: {
          name: 'ruby',
          homepage: true,
          color: colors.next(),
        }
      },
      ios: {
        sortBy: 'date',
        reverse: true,
        metadata: {
          name: 'ios',
          homepage: true,
          color: colors.next(),
        }
      },
      journal: {
        sortBy: 'date',
        reverse: true,
        metadata: {
          name: 'work journal',
          homepage: true,
          color: colors.next(),
        }
      },
      segment: {
        sortBy: 'date',
        reverse: true,
        metadata: {
          name: 'segment',
          homepage: true,
          color: colors.next(),
        }
      },
      googlechrome: {
        sortBy: 'date',
        reverse: true,
        metadata: {
          name: 'google chrome',
          homepage: true,
          color: colors.next(),
        }
      },
      books: {
        sortBy: 'date',
        reverse: true,
        metadata: {
          name: 'books',
          homepage: true,
          color: colors.next(),
        }
      },
      design: {
        sortBy: 'date',
        reverse: true,
        metadata: {
          name: 'design',
          homepage: true,
          color: colors.next(),
        }
      },
      mac: {
        sortBy: 'date',
        reverse: true,
        metadata: {
          name: 'mac',
          homepage: true,
          color: colors.next(),
        }
      },
      zsh: {
        sortBy: 'date',
        reverse: true,
        metadata: {
          name: 'zsh',
          homepage: true,
          color: colors.next(),
        }
      },
      xcode: {
        sortBy: 'date',
        reverse: true,
        metadata: {
          name: 'xcode',
          homepage: true,
          color: colors.next(),
        }
      },
    }))
    .use(tags())
    .use(partials({
      directory: 'partials'
    }))
    .use(branch('**/*.md')
         .use(metallic())
         .use(markdown({
           smartypants: true,
           gfm: true,
           mangle: false,
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
      frontmatter: true,
      redirections: {
        '/b/2012/12/overriding-uiviewcontrollers-view-property-done-right': '/b/2012/12/overriding-uiviewcontroller-s-view-property-done-right/'
      }
    }))
    .use(excerpt({
      maxLength: 160,
      ellipsis: '…'
    }))
    .use(feed({
      collection: 'articles',
      preprocess: function(file) {
        file.categories = file.collections
        return file
      }
    }))
    .use(layouts({
      directory: 'layouts',
      engine: 'handlebars',
      pattern: '**/*.html',
      default: 'post.html'
    }))

if (process.env.WATCH) {
  pipe = pipe.use(browserSync({
    server: 'build',
    files : ['src/**/*', 'layouts/**/*', 'partials/**/*']
  }));
}

pipe.build(function(err) {
  if (err) throw err
});
