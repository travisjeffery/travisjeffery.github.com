---
layout: post.html
title: "Basic authentication with AFNetworking 2"
date: 2013-09-27 23:39
comments: true
categories: ios objc c mac afnetworking authentication
---

Use `-[AFHTTPRequestSerializer setAuthorizationHeaderFieldWithUsername:password:]` on `-[AFHTTPSessionManager requestSerializer]`.

For example, in your AFHTTPSessionManager subclass:

``` objc
@implementation MyHTTPSessionManager

- (instancetype)initWithBaseURL:(NSURL *)url {
    self = [super initWithBaseURL:url];
    if (self) {
        [self.requestSerializer setAuthorizationHeaderFieldWithUsername:@"username" password:@"password"];
    }
    return self;
}

@end
```
