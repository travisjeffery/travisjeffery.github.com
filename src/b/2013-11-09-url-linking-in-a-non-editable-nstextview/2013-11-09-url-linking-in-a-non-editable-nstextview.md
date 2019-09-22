---
layout: post.html
title: "URL Linking in a Non-Editable NSTextView"
date: 2013-11-09 01:39
comments: true
categories: appkit detection link mac nstextview
---

You’re likely here because you thought you could just do this:

``` objc
NSTextView *textView = [NSTextView new];
[textView setEditable:NO];
[textView setAutomaticLinkDetectionEnabled:YES];
[textView setString:@"homesite: http://travisjeffery.com/ and twitter: http://twitter.com/travisjeffery"];
// ...
```

And you’d have clickable links in your NSTextView. Nope. setAutomaticLinkDetectionEnabled: works only when the NSTextView is editable.

The simplest solution is to build an NSAttributedString with links found using an NSDataDetector. Like so:

``` objc
[textView.textStorage setAttributedString:[self autoLinkURLs:@"homesite: http://travisjeffery.com/ and twitter: http://twitter.com/travisjeffery"]];

// ..

- (NSAttributedString *)autoLinkURLs:(NSString *)string {
    NSMutableAttributedString *linkedString = [[NSMutableAttributedString alloc] initWithString:string];

    NSDataDetector *detector = [NSDataDetector dataDetectorWithTypes:NSTextCheckingTypeLink error:nil];
    [detector enumerateMatchesInString:string options:0 range:NSMakeRange(0, string.length) usingBlock:^(NSTextCheckingResult *match, NSMatchingFlags flags, BOOL *stop) {
        if (match.URL) {
            NSDictionary *attributes = @{ NSLinkAttributeName: match.URL };
            [linkedString addAttributes:attributes range:match.range];
        }
    }];

    return [linkedString copy];
}
```
