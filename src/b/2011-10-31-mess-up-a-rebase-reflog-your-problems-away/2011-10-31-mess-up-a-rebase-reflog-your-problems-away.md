---
layout: post.html
title: "Mess up a rebase? reflog your problems away"
date: 2011-10-31 22:47
comments: false
categories: git rebase reflog
---

There is no reason not to rebase your topic branches onto the mainline
branches, i.e. dev/ master, if you follow the git flow model.  The reason to
rebase is to have a neat, simple and tidy history.

If you're afraid of doing a bad, here's why it's just as easy to get yourself
out of a bad rebase as it is a bad merge, thanks to the mythical *reflog*.

## Monday morning meltdown, an example

So, let's say it's Monday morning you come into finish up working on release
ticket, and you do what I would call: "a bad", and rebase your topic branch onto dev when you
actually intended to rebase your topic branch onto release, so it goes...

Keep calm and carry on. We can easily solve this by looking at the reflog,
finding the commit you made before you rebased and the resetting hard back to
that commit.

Here's a example to make things crystal clear:

This is an example of the output caused by invoking `git reflog`. Reading from
the bottom to the top you can follow the history of actions I made.

[![Reflog](http://media.tumblr.com/tumblr_ltynbgl5vG1qck115.png)](http://i.imgur.com/4763S.png)

1. I made a new repo and initial commit with the message: "Initial commit in master." (@{10})
2. I make a couple of branches, dev and my_topic_branch (@{9}-@{6})
3. I make a commit in my dev branch with the message: "Making a newer commit in dev." (@{5})
4. I goto my topic branch and make a commit that I know will cause a conflict
   with the commit I just made in dev, the commit in my topic branch has the message: "Making the newest commit in my_topic_branch." (@{3})
5. I then rebase my topic branch onto dev, fix the conflict I constructed and finish
   the rebase. (@{3}-@{0})

So this is what the history looks like in my topic branch after rebasing my
topic branch onto dev:

[![After rebasing](http://media.tumblr.com/tumblr_ltynbxR4Mt1qck115.png)](http://i.imgur.com/5TLp5.png)

This brings us to the present. I realize that I made a mistake by rebasing my
topic branch onto dev and want to go back to the commit I made in my topic
branch prior to rebasing:

`git reset --hard HEAD@{5}`

And my topic branch is once again in the state in which it was before I rebased:

[![Before rebasing](http://media.tumblr.com/tumblr_ltyncagHDc1qck115.png)](http://i.imgur.com/ptL10.png)

Crisis averted.
