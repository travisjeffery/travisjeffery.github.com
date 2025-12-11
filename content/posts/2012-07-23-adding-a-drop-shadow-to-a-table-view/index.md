---
title: "Adding a drop shadow to a table view"
date: 2012-07-23T00:00:00Z
tags: ["ios"]
aliases:
  - /b/2012/07/adding-a-drop-shadow-to-a-table-view/
---
Recently I was implementing a view where the last
cell of a table view needed a drop shadow.

The idea of the implementation was to use the shadow properties on the
table cell's Core Animation layer to render our drop shadow. 

(cell references the last cell of the table view)
```
- (UITableViewCell *)tableView:(UITableView *)tableView
  cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
  // ...
  cell.layer.shadowOffset = CGSizeMake(0, 15);
  cell.layer.shadowColor = [[UIColor blackColor] CGColor];
  cell.layer.shadowRadius = 3;
  cell.layer.shadowOpacity = .75f;
  CGRect shadowFrame = cell.layer.bounds;
  CGPathRef shadowPath = [UIBezierPath bezierPathWithRect:shadowFrame].CGPath;
  cell.layer.shadowPath = shadowPath;
  // ...
}
```

The shadow path is set for performance reasons, by setting it you remove the
need to blur the layers underneath the table view cell.

You can change the drop shadow style by messing around with it's properties,
perhaps decreasing the opacity to have a lighter shadow, increasing the radius
to have a longer shadow, etc.

<img src="images/people-list-view.png">

