---
layout: post.html
title: "Getting the index path of a table view cell via a subview event"
date: 2012-07-22 16:55
comments: false
categories: ios uitableviewcell table-view-cell indexpath
---

Let's say you've subclassed UITableViewCell such that you have added a UIButton as a
subview, and whenever you touch that button you want to perform some action on
the data source of your UITableView. To do that you probably want to figure
out what index path is associated with the pressed button.

Here's one way, the idea is to add a target and action to the
button of the cell for when it's pressed, and then in that action get the index
path by having the table view tell us what index path is associated with
the point that was touched.

Add the target and action to the button of the cell for when it's pressed,

```objective-c
- (UITableViewCell *)tableView:(UITableView *)tableView
  cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
  // ...
  [cell.myButton addTarget:self action:@selector(touchMyButton:event:) forControlEvents:UIControlEventTouchUpInside];
  // ...
}
```

Have the table view tell us what index path is associated with the point that was touched,

```objective-c
- (void)touchMyButton:(UIButton*)button event:(UIEvent*)event
{
    NSIndexPath* indexPath = [_tableView indexPathForRowAtPoint:
                                  [[[event touchesForView:button] anyObject]
                                  locationInView:_tableView]];
    // ... 
}
```
