---
title: "Xcode attaching to app running in simulator not working"
date: 2013-10-03T00:00:00Z
tags: ["ios"]
---
If you're running your app in Xcode and the simulator, they may hang saying `Attaching to your app name...`.

To fix this and run your app in the simulator with the lldb debugger, go into your app's target, and explicitly set the deployment target to the version of the simulator to run. For me, right now, that's `7.0`. If left blank, or with the placeholder, Xcode isn't smart enough to figure it out.

![Settings to fix xcode attaching problem](images/xcode-attaching.png)

Editing the scheme and setting the debugger to none works too, but then you don't have a debugger.
