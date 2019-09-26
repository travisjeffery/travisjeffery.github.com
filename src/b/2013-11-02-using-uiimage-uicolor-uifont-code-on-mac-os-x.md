---
layout: post.html
title: "Using UIImage, UIColor, UIFont Code on Mac OS X"
date: 2013-11-02 20:40
comments: true
collection: ios
---

This week I switched from working on iOS apps at 37signals to working on a similar mac app. I wanted to shared code between the ios and mac app, this is easy to do with foundation classes - my model and networking code. But doesn't work right out of the box for stuff like images, colors, fonts, since they're either in UIKit or AppKit. Thankfully you can adapt code for images, colors, and bezier paths using #define. Like so:

``` objc
#if TARGET_OS_IPHONE

#define TRVSColor UIColor
#define TRVSImage UIImage
#define TRVSFont UIFont
#define TRVSBezierPath UIBezierPath

#elif TARGET_OS_MAC && !TARGET_OS_IPHONE

#define TRVSColor NSColor
#define TRVSImage NSImage
#define TRVSFont NSFont
#define TRVSBezierPath NSBezierPath

#endif
```

Those are the only classes you can do this with.

Throw that code in something like `TRVSPlatformAdapter.h`.

Often in apps I write, I'll put category methods UIColor/NSColor for colors often used in the app's design.

This is how this is done while still being platform independent.

Have `Color+TRVSKit.{h, m}` like so:

``` objc
#import "TRVSPlatformAdapter.h"

@interface TRVSColor (TRVSKit)

+ (TRVSColor *)trvs_colorWithHexString:(NSString *)hexString;

@end

//

#import "Color+TRVSKit.h"

@implementation TRVSColor (TRVSKit)

+ (TRVSColor *)trvs_colorWithHexString:(NSString *)hexString {
  // ...
  return [TRVSColor colorWithRed:red green:green blue:blue alpha:alpha];
}

```

When this code is compiled for ios, TRVSColor will be compiled as UIColor, on os x: NSColor.
