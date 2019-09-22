---
layout: post.html
title: "Async testing with Xcode and any testing framework such as XCTest, SenTestingKit, Expecta, etc."
date: 2013-10-11 17:54
comments: true
categories: objc ios mac async testing xctest
---

I wrote [TRVSMonitor](https://github.com/travisjeffery/TRVSMonitor), a synchronization construct with the ability to wait until signalled that a condition was met.

This makes asynchronous testing easy. TRVSMonitor works with any testing framework too.

``` objc
@interface APIClientTests : XCTestCase
@property (nonatomic, strong, readwrite) NSURLSession *URLSession;
@end

@implementation APIClientTests

- (void)setUp {
    self.URLSession = [NSURLSession sessionWithConfiguration:[NSURLSessionConfiguration defaultSessionConfiguration]];
}

- (void)testAPIEndpoint {
    __block NSDictionary *JSON = nil;
    __block TRVSMonitor *monitor = [TRVSMonitor monitor];

    [self.URLSession dataTaskWithRequest:[NSURLRequest requestWithURL:[NSURL URLWithString:@"http://127.0.0.1:8000"]] completionHandler:^(NSData *data, NSURLResponse *response, NSError *error) {
        JSON = [NSJSONSerialization JSONObjectWithData:data options:0 error:NULL];
        [monitor signal];
    }];

    [monitor wait];

    XCTAssert(JSON);
    XCTAssertEqualObjects(@"1", JSON[@"id"]);
    XCTAssertEqualObjects(@"travis jeffery", JSON[@"name"]);
}

@end
```

Check the [readme](https://github.com/travisjeffery/TRVSMonitor) for the deets.
