---
title: "Making Custom Transitions Between UIViewControllers"
date: 2012-10-22T00:00:00Z
tags: ["ios"]
---
I released a project called
[TRVSNavigationControllerTransition](https://github.com/travisjeffery/TRVSNavigationControllerTransition).
The project adds convenient methods to translate the entire UINavigationController's view while
pushing and popping UIViewControllers to and from UINavigationControllers, rather than translating
the viewController's view --- which is how UINavigationController's pushViewController:animated:
works.

## Example

These images illustrate the difference. In the first image, the navigation controller translate's the view controller's view. The problem: if the view controller that's pushed hides the navigation bar, then the navigation bar will suddenly and awkwardly hide during the push.

![Bad](https://raw.github.com/travisjeffery/TRVSNavigationControllerTransition/master/Bad.gif)

In the second image, using TRVSNavigationControllerTransition, the navigation controller translate's the navigation controller's view. So the navigation bar remains view until the animation's finished.

![Good](https://raw.github.com/travisjeffery/TRVSNavigationControllerTransition/master/Good.gif)

## How to make your own transition

TRVSNavigationControllerTransition works like this:

1. Take a snapshot of the current view in the form of a CALayer and add it as a sublayer
of the current view.
2. Push or pop the next view without animation.
3. Take a snapshot of the new view in the form of a CALayer.
4. Add whatever animations you want to those layers for their transition.
5. Remove the layers from their superlayer once the transition animation finishes.

See
[UINavigationController+TRVSNavigationControllerTransition.m](https://github.com/travisjeffery/TRVSNavigationControllerTransition/blob/master/UINavigationController%2BTRVSNavigationControllerTransition.m) for more
details.

## Rejected Alternative

I saw others using a CATransition, like so:

    CATransition* animation = [CATransition animation];
    animation.duration = 0.3f;
    animation.type = kCATransitionPush;
    animation.subtype = kCATransitionFromRight;

The problem is that kCATransitionPush's animation looks different from UINavigationController's pushViewController:animated:. It doesn't fit.

## Install

Grab the project at [GitHub
repo](http://github.com/travisjeffery/TRVSNavigationControllerTransition), or
with the [CocoaPod spec](https://github.com/travisjeffery/TRVSNavigationControllerTransition/blob/master/TRVSNavigationControllerTransition.podspec) using the name: `TRVSNavigationControllerTransition`.

## Use

To use TRVSNavigationControllerTransition, link your binary
with the QuartzCore.framework library. Then in your code write:

	[self.navigationController pushViewControllerWithNavigationControllerTransition:viewController];

	[self.navigationController popViewControllerWithNavigationControllerTransition];
