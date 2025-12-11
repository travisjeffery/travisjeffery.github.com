---
title: "Basic authentication with AFNetworking 2"
date: 2013-09-27T00:00:00Z
tags: ["ios"]
aliases:
  - /b/2013/09/basic-authentication-with-afnetworking-2/
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
