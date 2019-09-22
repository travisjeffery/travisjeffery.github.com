---
layout: post.html
title: "Using TextKit to Put an Image in a Text View"
date: 2013-10-20 01:23
comments: true
categories: ios textkit uitextview uiimage image text kit
---

Boom goes the dynamite.

``` objc
NSTextAttachment *attachment = [[NSTextAttachment alloc] initWithData:nil ofType:nil];
attachment.image = [UIImage imageNamed:@"whatever"];
NSAttributedString *attributedString = [NSAttributedString attributedStringWithAttachment:attachment];
self.textView.attributedText = attributedString;
```
