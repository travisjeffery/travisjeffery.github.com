---
layout: post.html
title: "Testing JavaScript projects with Grunt, Jasmine, and JSHint"
date: 2013-09-03 22:30
comments: false
categories: javascript jshint grunt jasmine jasmine-jquery travis-ci github ci npm node
---

I maintain jasmine-jquery, a library providing jquery matchers and fixture loading for jasmine. Recently, I setup jasmine-jquery with [grunt](http://gruntjs.com/), a javascript task runner. This way, I can run the test suite from the command-line, and have continuous integration with travis-ci — so collaborators know when they broke something. In the process of setting all this up, I learned about grunt, and using grunt with jshint and jasmine.

To use grunt with jamine, jshint, and travis-ci, you need four files: package.json, Gruntfile.js, .jshintrc, and .travis.yml.

First, you need a package.json file in the root of your project. [That'll look like](https://github.com/velesin/jasmine-jquery/blob/master/package.json):

``` json
{
  ...
  , ...
  , "scripts": { "test": "grunt test" }
  , "devDependencies": {
      "grunt": "~0.4.1"
    , "grunt-contrib-jshint": "~0.6.0"
    , "grunt-contrib-jasmine": "~0.4.0"
  }
}
```

[travis-ci runs `npm test`](http://about.travis-ci.org/docs/user/languages/javascript-with-nodejs/#Default-Test-Script), and now `npm test` will run `grunt test`.

For grunt, you need a [Gruntfile.js](https://github.com/velesin/jasmine-jquery/blob/master/Gruntfile.js):

``` javascript
/* jshint node: true */

module.exports = function (grunt) {
  "use strict";

  grunt.initConfig({
      pkg: grunt.file.readJSON('package.json')
    , jshint: {
        all: [
            "Gruntfile.js"
          , "lib/**/*.js"
          , "spec/**/*.js"
        ]
      , options: {
          jshintrc: '.jshintrc'
        },
      }
    , jasmine: {
        src: "lib/**/*.js"
      , options: {
          specs: "spec/**/*.js"
        , vendor: "vendor/**/*.js"
      }
    }
  })

  grunt.loadNpmTasks('grunt-contrib-jshint')
  grunt.loadNpmTasks('grunt-contrib-jasmine')

  grunt.registerTask('test', ['jshint', 'jasmine'])
  grunt.registerTask('default', ['test'])
};
```

See [grunt-contrib-jasmine's README](https://github.com/gruntjs/grunt-contrib-jasmine) for the available options you can set.

`grunt test` runs our test task, this checks the code's quality with jshint, then runs the tests with jasmine. [jasmine-jquery's .jshintrc](https://github.com/velesin/jasmine-jquery/blob/master/.jshintrc).

To setup travis-ci, you need a [.travis.yml file](https://github.com/velesin/jasmine-jquery/blob/master/.travis.yml):

``` yaml
language: node_js
node_js:
  - 0.8
before_script:
  - npm install -g grunt-cli
```

[Integrate travis-ci with your project on GitHub.](http://about.travis-ci.org/docs/user/getting-started/#Step-one%3A-Sign-in)

Fin.
