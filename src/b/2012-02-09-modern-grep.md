---
layout: post.html
title: "Modern grep"
date: 2012-02-09 03:27
comments: false
collection: tools
---

While grep reigned as the preeminent text search tool for a long time, its overly unopinionated
approach to defaults and maintaining backwards compatibility allowed new tools --- namely; ack,
the silver searcher, and ripgrep --- to gain users and encroach on grep's territory.

For example, git stores unreadable blobs under the .git directory in your repos and it doesn't make
sense to search these files. However, grep doesn't ignore these files by default unlike ack and
ripgrep.

On average, a search by a newbie ack user will be faster than the same search by a newbie grep user,
despite the fact that grep is written in C and ack in Perl, because ack conveniently ignores folders
and files you probably don't want searched --- like .git or the files listed in your .gitignore.

> I feel the need...the need for speed!

With some grep know-how, we can make grep faster and behave like these modern search tools.

## Exclude Directories

grep can exclude directories that it searches, increasing its speed substantially. The following excludes the .git directory from its search:

```
$ grep --exclude-dir=.git
```

This speeds up searches by a lot, I ran two uncached searches in Rails's repo:

```
$ grep -r "class << self" .

$ grep -rIPs --exclude-dir=.[a-zA-Z0-9]* --exclude=.* --exclude=*~ "class << self" .
```

He former, non-excluding, grep took 6.009s. The
latter, excluding, grep took 2.235s.

## Perl Regular Expressions

Modern search tools like ack support the popular Perl regular expressions. By default, grep uses
the less known POSIX regular expressions.

For example, let's say we want to match a phone number and capture its area
codes.

The Perl regular expression:

```
(\d{3})-\d{3}-\d{4}
```

The POSIX regular expression:

```
\([0-9]\{3\}\)-[0-9]\{3\}-[0-9]\{4\}
```

Fortunately, you can use Perl regular expressions with grep by giving it the
`-P` or `--perl-regexp` argument.

```
grep -P "(\d{3})-\d{3}-\d{4}"
```

## Useful Defaults

Having to give grep all these arguments would be a drag, to configure grep to exclude hidden directories and use Perl regular expressions by default, set the shell variable `GREP_OPTIONS`:

`export GREP_OPTIONS='-rIPs --exclude-dir=.[a-zA-Z0-9]* --exclude=.* --exclude=*~ --color=auto'`

There's no argument to make grep organize its output like ack. Also, neither
integrates with git, but git has its own grep for searching your repos. You can read my post on [searching git like a ninja](/b/2012/02/search-a-git-repo-like-a-ninja/) to learn about `git grep` and get the best of both grep and ack.

## Sources and further reading

- [why GNU grep is fast](http://lists.freebsd.org/pipermail/freebsd-current/2010-August/019310.html)
- [History of grep](http://en.wikipedia.org/wiki/Grep#History) (including Ken Thompson's inspiration for the name: ed's `g/re/p` — similar to the `:g/re/p` Vim user's have today!)
- you will need grep version >= 2.5.3 to use `--exclude-dir`
