---
layout: post.html
title: "Modern Grep"
date: 2012-02-09 03:27
comments: false
categories: grep regexp posix perl
---

We read a lot more code than we write, and more often than not we have some
notion of what we're looking for. There have been many programs and algorithms
developed in-order to enhance our ability to find text and be productive, but really the
giant whose usage has been strong from its inception in 1973 till today is
grep.

grep is an essential tool to know, but unfortunately it has not kept up with the
times in terms of its usage in respect to how we build and version our
applications. For example, the majority of data contained within the folder
of a git repo are unreadable binary large objects. It doesn't make sense to
search these files but grep doesn't know this, a more recent program called ack
does.

On average, a search by a newbie ack user will be faster than the same search by
a newbie grep user. This is because ack conveniently ignores folders and files
you probably don't want to be searched, these ignored folders include .git,
the folder that git uses as a database for your repository.

<blockquote>I feel the need...the need for speed!</blockquote>

grep can also exclude searching directories, including .git, to increase its speed
remarkedly:

`grep --exclude-dir=.git`

This can be tremendous boon for speeding up searches, I did two uncached searches in rails's repo:

`grep -r "class << self" .`

`grep -rIPs --exclude-dir=.[a-zA-Z0-9]* --exclude=.* --exclude=*~ "class << self" .`

With the former, non-excluding grep search I had a time of 6.009s and with the
latter, excluding grep search 2.235s. In general the speed increase is in
the range of 2-3x faster.


Another benefit to using ack is being able to use the widely known and copied
Perl regular expressions rather than the older and now less known POSIX regular
expressions.

For example, let's say we want to match phone numbers and capture the area
code:

Here it is in a Perl regular expression:

`(\d{3})-\d{3}-\d{4}`

And the equivalent POSIX:

`\([0-9]\{3\}\)-[0-9]\{3\}-[0-9]\{4\}`

Thankfully, you can actually use Perl regular expressions with grep, by giving
either a `-P` or `--perl-regexp` argument.

`grep -P "(\d{3})-\d{3}-\d{4}"`

To configure grep such that you don't need to call grep with these arguments
each time, you can set the shell variable `GREP_OPTIONS` by putting into your
.zshrc or .bashrc:

`export GREP_OPTIONS='-rIPs --exclude-dir=.[a-zA-Z0-9]* --exclude=.* --exclude=*~ --color=auto'`

The biggest downfall with grep vs. ack that really can't be fixed by arguments,
is how ack nicely organizes its output, also neither integrates with git...

git users should check out my [post](/b/2012/02/search-a-git-repo-like-a-ninja/) on searching repos with git grep! I show
how you can have the best of both grep and ack!

## Sources and further reading

- [why GNU grep is fast](http://lists.freebsd.org/pipermail/freebsd-current/2010-August/019310.html)
- [History of grep](http://en.wikipedia.org/wiki/Grep#History) (including Ken Thompson's inspiration for the name: ed's `g/re/p` — similar to the `:g/re/p` Vim user's have today!)
- you will need grep version >= 2.5.3 to use `--exclude-dir`
