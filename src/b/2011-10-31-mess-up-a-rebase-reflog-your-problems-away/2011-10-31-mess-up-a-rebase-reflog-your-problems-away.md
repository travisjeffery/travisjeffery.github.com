---
layout: post.html
title: "Mess up a rebase? Reflog your problems away"
date: 2011-10-31 22:47
comments: false
collection: git
---

I'm going to show you how to use the reflog to fix mistakes you've made with Git, where you seemingly can't recover the history.

People fear Git, fear making a mistake that ruins their repo, and fear the ensuing embarrassment. Some people fear rebasing so much that they only merge. I'm going to use a botched rebase as an example of how you can recover from anything with the reflog.

Let's say you've just finished working on a feature that you have in a topic branch and then you accidentally rebased your topic branch onto dev when you meant to rebase onto release. Furthermore, you messed up a merge conflict and no longer have access to the commit you need reset to.

With the reflog you can find commits that seem to be unrecoverable. Run the following to see the reflog:

```
$ git reflog
```

Here's an example of the reflog's output --- reading from the bottom to the top, you can follow the
history of the repo and the actions I made.

![Reflog](http://i.imgur.com/4763S.png)

1. I made a new repo and initial commit with the message: "Initial commit in master." (@{10})
2. I make a couple of branches, dev and my_topic_branch (@{9}-@{6})
3. I make a commit in my dev branch with the message: "Making a newer commit in dev." (@{5})
4. I switch to my topic branch and make a commit that I know will cause a conflict
   with the commit I just made in dev. The commit in my topic branch has the message: "Making the newest commit in my_topic_branch." (@{3})
5. I rebase my topic branch onto dev, fix the conflict and finish
   the rebase. (@{3}-@{0})

This is what the history looks like in my topic branch after rebasing onto dev:

![After rebasing](http://i.imgur.com/5TLp5.png)

This is the point where you would have realized that you made a mistake by rebasing your topic branch onto dev and that you want to go back to the commit prior to rebasing. By looking at the reflog, we see that commit is HEAD@{5}. All that's left is to reset our topic branch back to that commit by running the following:

```
$ git reset --hard HEAD@{5}
```

After running the command, my topic branch is back to the commit before I rebased:

![Before rebasing](http://i.imgur.com/ptL10.png)

Crisis averted.
