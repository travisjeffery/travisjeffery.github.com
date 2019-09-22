---
layout: post.html
title: "Piping into a Docker container"
date: 2015-09-25 20:16
comments: false
categories: docker shell unix pipes
---

Here's how you can write docker images that you can pipe into:

Dockerfile, here I'm installing the go programs I'm going to run and pipe into:

``` sh
FROM golang
RUN go get github.com/segmentio/throttle
RUN go get github.com/segmentio/json_to_nsq
COPY entrypoint.sh /entrypoint.sh
CMD ["/bin/sh", "/entrypoint.sh"]
```

entrypoint.sh, here I'm reading from stdin and piping into the programs I want to run:

``` sh
rate=${2:-50}
addr=${3:-nsqd:4150}

echo "Sending events to $addr at the rate of $rate/s"

cat - \
    | throttle $rate \
    | json_to_nsq -t events -a "$addr"
```

And here's how to run it (assuming the image is called `events`):

``` sh
cat events.json | docker run -it events
```
