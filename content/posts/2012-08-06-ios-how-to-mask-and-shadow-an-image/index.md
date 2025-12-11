---
title: "iOS how-to: mask and shadow views"
date: 2012-08-06T00:00:00Z
tags: ["ios"]
aliases:
  - /b/2012/08/ios-how-to-mask-and-shadow-views/
---
Two techniques that iOS developers use to make visually appealing app are masks and shadows; for
example, masking an image to have round corners, or adding a drop shadow to an image to have
depth. Implementing these techniques separately is trivial, implementing these techniques together
is tricky.

To both mask and shadow any view, let's use an image as an example, you:

- create a new layer whose layer has a shadow.
- mask the image's layer.
- add the image's layer as a sublayer of the shadow layer.
- add the shadow layer as a sublayer of the view that you want to show the image in.

I've created a [project on
GitHub](https://github.com/travisjeffery/ios-how-to-mask-and-shadow), and
[wrote my
commits](https://github.com/travisjeffery/ios-how-to-mask-and-shadow/commits/master/)
in such a way as to see the stages of building our final result.

We start with an image as a subview of our view with no
changes other than centering it.

<img src="images/mask-and-shadow-1.png">

``` objc
//
//  TJViewController.m
//  MaskAndShadow
//
//  Created by Travis Jeffery on 2012-08-06.
//  Copyright (c) 2012 Travis Jeffery. All rights reserved.
//

#import "TJViewController.h"

@interface TJViewController ()

@end

@implementation TJViewController

- (void)viewDidLoad
{
    [super viewDidLoad];

    // white bg to see the shadow easier
    self.view.backgroundColor = [UIColor whiteColor];

    // the image we're going to mask and shadow
    UIImageView* image = [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"sj.jpeg"]];
    image.center = self.view.center;

    [self.view addSubview:image];
}

@end
```

Then we turn our image into a circle by masking its corners.

<img src="images/mask-and-shadow-2.png">

``` objc
//
//  TJViewController.m
//  MaskAndShadow
//
//  Created by Travis Jeffery on 2012-08-06.
//  Copyright (c) 2012 Travis Jeffery. All rights reserved.
//

#import "TJViewController.h"

@interface TJViewController ()

@end

@implementation TJViewController

- (void)viewDidLoad
{
    [super viewDidLoad];

    // white bg to see the shadow easier
    self.view.backgroundColor = [UIColor whiteColor];

    // the image we're going to mask and shadow
    UIImageView* image = [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"sj.jpeg"]];
    image.center = self.view.center;

    // use the image's layer to mask the image into a circle
    image.layer.cornerRadius = roundf(image.frame.size.width/2.0);
    image.layer.masksToBounds = YES;

    [self.view addSubview:image];
}

@end
```

If we added the shadow to the image's layer, the mask on the image's layer would cut off the shadow. Instead, we add the shadow to the parent layer of the image. And then we add that shadow layer to the view controller's view layer.

<img src="images/mask-and-shadow-3.png">

``` objc
//
//  TJViewController.m
//  MaskAndShadow
//
//  Created by Travis Jeffery on 2012-08-06.
//  Copyright (c) 2012 Travis Jeffery. All rights reserved.
//

#import "TJViewController.h"
#import <QuartzCore/QuartzCore.h>

@interface TJViewController ()

@end

@implementation TJViewController

- (void)viewDidLoad
{
    [super viewDidLoad];

    // white bg to see the shadow easier
    self.view.backgroundColor = [UIColor whiteColor];

    // the image we're going to mask and shadow
    UIImageView* image = [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"sj.jpeg"]];
    image.center = self.view.center;

    // make new layer to contain shadow and masked image
    CALayer* containerLayer = [CALayer layer];
    containerLayer.shadowColor = [UIColor blackColor].CGColor;
    containerLayer.shadowRadius = 10.f;
    containerLayer.shadowOffset = CGSizeMake(0.f, 5.f);
    containerLayer.shadowOpacity = 1.f;

    // use the image's layer to mask the image into a circle
    image.layer.cornerRadius = roundf(image.frame.size.width/2.0);
    image.layer.masksToBounds = YES;

    // add masked image layer into container layer so that it's shadowed
    [containerLayer addSublayer:image.layer];

    // add container including masked image and shadow into view
    [self.view.layer addSublayer:containerLayer];
}

@end
```
