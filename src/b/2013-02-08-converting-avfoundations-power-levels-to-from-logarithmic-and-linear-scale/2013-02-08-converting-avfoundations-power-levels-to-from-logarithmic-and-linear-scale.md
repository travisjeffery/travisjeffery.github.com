---
layout: post.html
title: "Converting avfoundation's power levels to/from logarithmic and linear scale"
date: 2013-02-08 17:09
comments: true
categories: ios avfoundation audio video core-audio
---

When using AVFoundation, you'll notice that the numbers returned when checking the audio channel power levels may look kind of strange. The audio levels returned to you when calling `AVCaptureSession-averagePowerLevel` or `AVCaptureAudioChannel-averagePowerLevel`, etc. are in a logarithmic scale from -160dB to 0dB, similar to how we perceive sound. 

But you may want to convert this logarithmic scale to a linear scale from 0.0 to 1.0 to use in an interface  or something, here's how to do it:

``` objective-c
CGFloat linearPowerLevel = powf(10.f, decibelPowerLevel / 20.f);
```

Here's how to go the other way:

``` objective-c
CGFloat decibelPowerLevel = log10f(linearPowerLevel) * 20.f;
```
