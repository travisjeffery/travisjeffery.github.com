---
layout: post.html
title: "Overriding UIViewController's view property, done right"
date: 2012-12-28 10:47
collection: ios
---

I read ***a lot*** of code, and some of the most common mistakes I see is how people override `UIViewController`'s view property.

Here's how it ***should*** be done, in this example we're replacing `UIViewController`'s view property (a `UIView`) with a `UIScrollView`:

``` objective-c
// ViewController.h
@interface ViewController : UIViewController

@property (strong, nonatomic) UIScrollView *view;

@end

// ViewController.m
@implementation ViewController

@dynamic view;

- (void)loadView {
	self.view = [[UIScrollView alloc] initWithFrame:UIScreen.mainScreen.applicationFrame];
}

@end

```

Common mistakes include:

- Calling `[super loadView]`, which just wastes resources and Apple's documentation says not to do.
- Setting the view in `-viewDidLoad:`, which wastes resources again.
- Not providing both the implementation **and** type for the view property, and having to cast self.view everywhere

Note, if you use Interface Builder and have an associated XIB file then by default `-loadView` will take view from the XIB and load it as the `UIViewController`'s view. So think of `-loadView` as doing the job that a XIB would do, e.g. setting up your initial view hierarchy. Any code that wouldn't change if you were to switch from using `-loadView` to a XIB should go in `-viewDidLoad:`.
