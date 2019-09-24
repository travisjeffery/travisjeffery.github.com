---
layout: post.html
title: "On visibility with microservices and monoliths"
date: 2015-10-08 03:12
comments: false
draft: true
collection: engineering
---

<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr">We replaced our monolith with micro services so that every outage could be more like a murder mystery.</p>&mdash; Honest Status Page (@honest_update) <a href="https://twitter.com/honest_update/status/651897353889259520">October 7, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Obviously the "Honest Status Page" twitter account is having good fun, but the tweet's struct a chord with people who believe it. But based on my experiences of writing microservices and even monoliths, it makes no sense. Microservices greatly improves visibility over monolith applications.

The natural way to see a monolith is to see it through a single lens, but for any non-trivial application a single lens isn't enough.

Imagine having two broken cars, one that has a single "SHIT'S BROKEN YO" warning on your dashboard whenver anything is wrong with your car. The issue could be caused by several different things in various combinations so you have to Sherlock Holmes your way to find the root of the issue.

Compare that with car :dollar:, where each part of your car self-diagnoses and reports their issues to your dashboard. So when your car breaks down it is telling you where the point of failure is.

Catastropihc failures are typically the kind of issues people talk about, but even more interesting are subtle, minor issues that people don't look for that eventually cause a major issue. It's minor issues like these that I think microservices are even better at catching.

A catastrophic issue would be your main database going down completely. Either with monoliths or microservices you're going to know something is wrong right away, with a monolith you'll probably start by checking your logs which has a ton of other crap getting logged in there as well, but from there you see something is up with your database and you look into it. With a microservice, you'd have monitoring setup with your microservice and it would tell where the issue was.

But more illustrative of where microservices would indicate an issue better than a monolith app with a subtle issue. Let's say you have a redis db that serves as a cache for some kind of data in your app. And let's say that it's become slow for some reason. All that happens is that some part of your application becomes slower. With a monolith you might see a rise in your average response time, but again that response time is the sum of your whole app. It could be that someone added a bad query to your main database elsewhere, or that someone added a huge JS lib to your frontend. With microservices, because redis was it's own service and you had monitoring on the average response time of redis in-particular, you know where the issue is right away.

And yes, in your monolith you could build out similar monitoring. But that monitoring in itself can be complex and is responsible for that one piece of your infrastructure, so piling it all into one thing is poor design.
