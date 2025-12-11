---
title: "Using TextKit to put an image in a text view"
date: 2013-10-20T00:00:00Z
tags: ["ios"]
aliases:
  - /b/2013/10/using-textkit-to-put-an-image-in-a-text-view/
---
Boom goes the dynamite.

``` objc
NSTextAttachment *attachment = [[NSTextAttachment alloc] initWithData:nil ofType:nil];
attachment.image = [UIImage imageNamed:@"whatever"];
NSAttributedString *attributedString = [NSAttributedString attributedStringWithAttachment:attachment];
self.textView.attributedText = attributedString;
```
