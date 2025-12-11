---
title: "Scroll to the bottom of a UICollectionView"
date: 2013-09-19T00:00:00Z
tags: ["ios"]
aliases:
  - /b/2013/09/scroll-to-the-bottom-of-a-uicollectionview/
---
Here ya go.

``` obj-c
NSInteger section = [self numberOfSectionsInCollectionView:collectionView] - 1;
NSInteger item = [self collectionView:collectionView numberOfItemsInSection:section] - 1;
NSIndexPath *lastIndexPath = [NSIndexPath indexPathForItem:item inSection:section];
[collectionView scrollToItemAtIndexPath:lastIndexPath atScrollPosition:UICollectionViewScrollPositionBottom animated:YES];
```
