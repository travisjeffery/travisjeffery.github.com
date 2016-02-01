---
layout: post.html
title: "Quick staging and other file operations in git"
date: 2012-11-01 07:17
comments: false
categories: git shell zsh bash
---

## Introduction

Having a modular and well-organized code is clearly great from an architectural
standpoint, but it can make the actual filesystem layout and hierarchy of your
project a little complex, now that text editors and IDEs also have good
fuzzy finding capabilities you can largely not worry about this and still 
code efficiently. But when working with Git as your version control it does
help to be intimate with the filesystem layout of your project, or at least
have some tricks up your sleeve. In this post I'd like to share some tricks I
use.

## Staging files filtered matching some pattern

Most filenames in your project will be named after some convention, in Rails
projects most of the code associated with a user will fall under
`controllers/users_controller.rb`, `models/user.rb`, and
`views/users/*.html.erb`. And similarly in an iOS project you may have
something like `UsersViewController.{h,m}`, `User.{h,m}`.

So let's say we want to stage all the modified files associated with a user
really quickly, here's what I'd do:

```
git add `git ls-files --modified | grep -e "user.*"`
```

You can use ack instead of grep too, and I'd actually likely use ack myself.

`git ls-files` has the benefit of being very fast and smart since it already knows what
files are under version control and which files are modified, so it be much
faster than something like `find` which by default would search every file in
your project.

This technique can be used for a variety of things, let's say you staged all
modified files in your project when didn't mean to stage your controllers you
could do something like:

```
git reset `git ls-files | ack ".*_controller.rb"`
```

## Staging whole directories

Another trick I've found that people often don't know or take advantage of is
being able to run Git operations on whole directories.

So in the previous example where we unstaged all controller files, which would
likely all be in the same directory, `app/controllers` we could instead just
have done this:

`git reset app/controllers`

This technique works generally works with commands you've seen take a single
file.


I also recommend checking out a post I made earlier on [lots of tips for
searching Git repos](/b/2012/02/search-a-git-repo-like-a-ninja/).  Hopefully
this post has made you a more efficient Gitter, and if you have any other tips
please let me know.
