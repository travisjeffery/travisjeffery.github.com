---
layout: post.html
title: "Getting the status bar's height in iOS"
date: 2013-05-06 20:02
comments: false
collection: ios
---

I had someone ask me for the best way to get the status bar's height. Their problem was they were using UIApplication-statusBarFrame.size.height which will usually be 20.0f when in portrait (***but*** would be bigger if the user is on the phone, etc.) but when the phone was oriented in landscape the height was 480.0f.

The trick to the status bar's frame and height is to make sure you've converted it to the coordinate space of the view that you care about, this will probably be a UIViewController's view or subview.

``` objc
CGRect statusBarFrame = [yourView.window convertRect:UIApplication.sharedApplication.statusBarFrame toView:yourView];
CGFloat statusBarHeight = statusBarFrame.size.height;
```

Now you've got a height you'd expect—usually 20.0f.

I made a [demo app](https://github.com/travisjeffery/StatusBarDemo) that may make this concrete for you. Build &amp; Run, switch your device's orientation and watch the output in the Debug Area.
