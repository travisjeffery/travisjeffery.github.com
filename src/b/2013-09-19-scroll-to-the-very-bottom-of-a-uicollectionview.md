---
layout: post.html
title: "Scroll to the bottom of a UICollectionView"
date: 2013-09-19 22:57
comments: true
collection: ios
---

Here ya go.

``` obj-c
NSInteger section = [self numberOfSectionsInCollectionView:collectionView] - 1;
NSInteger item = [self collectionView:collectionView numberOfItemsInSection:section] - 1;
NSIndexPath *lastIndexPath = [NSIndexPath indexPathForItem:item inSection:section];
[collectionView scrollToItemAtIndexPath:lastIndexPath atScrollPosition:UICollectionViewScrollPositionBottom animated:YES];
```
