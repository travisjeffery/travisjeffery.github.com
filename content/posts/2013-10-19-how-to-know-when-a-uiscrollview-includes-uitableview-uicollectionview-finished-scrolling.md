---
title: "How to know when a UIScrollView (includes UITableView, UICollectionView) finished scrolling"
date: 2013-10-19T00:00:00Z
tags: ["ios"]
---
UIScrollViewDelegate has the method: `-[UIScrollViewDelegate scrollViewDidEndDragging:willDecelerate:]`, and the decelerate parameter is NO when the scroll view has finished scrolling.

So you could use it like this:

``` objc
- (void)scrollViewDidEndDragging:(UIScrollView *)scrollView willDecelerate:(BOOL)decelerate {
    if (!decelerate){
        NSLog(@"The scroll view isn't scrolling anymore.");
        // perform some animation
    }
}
```


