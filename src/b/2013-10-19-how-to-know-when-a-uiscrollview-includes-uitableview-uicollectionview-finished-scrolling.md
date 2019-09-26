---
layout: post.html
title: "How to know when a UIScrollView (includes UITableView, UICollectionView) finished scrolling"
date: 2013-10-19 16:53
comments: true
collection: ios
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


