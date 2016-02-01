---
layout: post.html
title: "Making custom transitions between uiviewcontrollers"
date: 2012-10-22 18:10
comments: false
categories:  ios objective-c uiviewcontroller uinavigationcontroller core-animation animations transitions
---

<strong>Note: iOS 7 has awesome APIs that make this sort of thing a lot funner, easier and powerful. When the SDK's NDA is over I'll be releasing some open source code and blog posts about them.</strong>

I just released a project called [TRVSNavigationControllerTransition](https://github.com/travisjeffery/TRVSNavigationControllerTransition) that adds convenience methods to
UINavigationControllers to push/pop UIViewControllers that translate the entire
UINavigationController's view rather than its viewController's view (which is
how UINavigationController's pushViewController:animated: behaves).

## Example

In the top example of the images below, only the view controller's view is translated so if the
pushed view controller hide's the navigation bar then the navigation bar in the
current view will suddenly disappear. In the bottom example using TRVSNavigationControllerTransition, the whole
navigation controller's view is translated in, and the navigation bar remains
correctly in the current view until the animation completes.

![Bad](https://raw.github.com/travisjeffery/TRVSNavigationControllerTransition/master/Bad.gif) ![Good](https://raw.github.com/travisjeffery/TRVSNavigationControllerTransition/master/Good.gif)

## Development and alternatives

Before, I tried and saw others using a CATransition, like so:

``` objective-c
CATransition* animation = [CATransition animation];
animation.duration = 0.3f;
animation.type = kCATransitionPush;
animation.subtype = kCATransitionFromRight;
```

The problem is that kCATransitionPush not only animates the
translations like you'd expect, but also the opacities of the views so the
transition looks differently from UINavigationController's pushViewController:animated:.

## Basic idea

The basic idea on how to make your own is pretty simple though,

1. take a snapshot of the current view in the form of a CALayer and add it as a sublayer
of the current view
2. push/pop the next view without animation
3. take a
snapshot of the new view in the form of a CALayer
4. add whatever animations you want to those layers to form their transition
5. remove the layers from their superlayer once the transition animation is complete

See
[UINavigationController+TRVSNavigationControllerTransition.m](https://github.com/travisjeffery/TRVSNavigationControllerTransition/blob/master/UINavigationController%2BTRVSNavigationControllerTransition.m) for more
details.

## Installing

You can grab the project via the [GitHub
repo](http://github.com/travisjeffery/TRVSNavigationControllerTransition), or
just via the [CocoaPod spec](https://github.com/travisjeffery/TRVSNavigationControllerTransition/blob/master/TRVSNavigationControllerTransition.podspec) with the name: `TRVSNavigationControllerTransition`,
but make sure you check for what the latest version is.

## Usage

To use TRVSNavigationControllerTransition just make sure your binary is linked
with the QuartzCore.framework library, and then to use:

``` objective-c
# to push, called just as you would with pushviewcontroller:animated:
[self.navigationController pushViewControllerWithNavigationControllerTransition:viewController];

# to pop called just as you would with popviewcontrolleranimated:
[self.navigationController popViewControllerWithNavigationControllerTransition];
```
