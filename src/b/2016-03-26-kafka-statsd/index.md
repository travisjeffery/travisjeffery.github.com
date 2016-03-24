---
layout: post.html
title: Graphing Kafka Offset Lags With StatsD
date: 2016-03-26 02:14
comments: false
draft: false
categories: kafka statsd
---

I wrote a [worker](https://github.com/travisjeffery/kafka-statsd) to track consumer offset lags with StatsD so that you
can graph them in Grafana or something similar.

<img class="img-fluid" src="images/graph.png" alt="Grafana example" />

It's written in Golang and there's a Docker image too, so it's easy to deploy and use.

[Check it out on GitHub.](https://github.com/travisjeffery/kafka-statsd)

