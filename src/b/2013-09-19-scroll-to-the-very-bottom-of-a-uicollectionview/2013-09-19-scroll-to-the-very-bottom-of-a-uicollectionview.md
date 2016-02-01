---
layout: post.html
title: "Scroll to the very bottom of a uicollectionview"
date: 2013-09-19 22:57
comments: true
categories: ios uicollectionview collection-view uikit uiscrollview
---

Here ya go.

``` obj-c
NSInteger section = [self numberOfSectionsInCollectionView:collectionView] - 1;
NSInteger item = [self collectionView:collectionView numberOfItemsInSection:section] - 1;
NSIndexPath *lastIndexPath = [NSIndexPath indexPathForItem:item inSection:section];
[collectionView scrollToItemAtIndexPath:lastIndexPath atScrollPosition:UICollectionViewScrollPositionBottom animated:YES];
```
