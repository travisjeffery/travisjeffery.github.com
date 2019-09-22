---
layout: post.html
title: "Library and Lambda function to show your Rdio heavy rotation on your website"
date: 2015-10-24 21:57
comments: false
categories: rdio js lambda node
---

I thought it'd be cool to show what albums I'm listening to lately on my site, so I wrote a client lib and
and Amazon Lambbda function to get the albums from your Rdio Heavy Rotation and put them on your site.

You can check it out on my [site](http://travisjeffery.com) under "the heavy rotation".

<img src="images/the-heavy-rotation.png" />

The Lambda function authenticates with Rdio and fetches the data for the client, and the client
adds the imgs to the web page.

Here's the [client code](https://github.com/travisjeffery/thr-client) on GitHub, and here's the [Lambda code](https://github.com/travisjeffery/thr-lambda) on GitHub.
