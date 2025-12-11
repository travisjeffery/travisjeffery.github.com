---
title: "Getting the index path of a table view cell via a subview event"
date: 2012-07-22T00:00:00Z
tags: ["ios"]
aliases:
  - /b/2012/07/getting-the-index-path-of-a-table-view-cell-via-a-subview-event/
---
You've subclassed UITableViewCell and you've added a UIButton as a subview. Whenever you touch that
button, you want to act on the data of your UITableView. To act on the data, you need to know the
index path of the cell containing the button. Here's how.

To find the index path of a touched subview; You add a touched event handler, then use the event to find the touch point in the table view, and then look up the index path at that point.

	- (UITableViewCell *)tableView:(UITableView *)tableView
	  cellForRowAtIndexPath:(NSIndexPath *)indexPath
	{
	  // ...
	  [cell.myButton addTarget:self action:@selector(touchMyButton:event:) forControlEvents:UIControlEventTouchUpInside];
	  // ...
	}

	- (void)touchMyButton:(UIButton*)button event:(UIEvent*)event
	{
	    NSIndexPath* indexPath = [_tableView indexPathForRowAtPoint:
	                                  [[[event touchesForView:button] anyObject]
	                                  locationInView:_tableView]];
	    // ...
	}
