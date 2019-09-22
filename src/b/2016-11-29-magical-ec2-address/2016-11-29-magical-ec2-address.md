---
layout: post.html
title: "EC2’S magical address to get instance metadata"
date: 2016-11-29 10:27
comments: true
categories: aws ec2 docker
---

There’s a magical address in EC2 that you can query to get metadata on that instance (`http://169.254.169.254`). What’s especially awesome about it, is that you can use it inside Docker containers which makes it an easy
way to find the host IP from inside the container without having to pass it in via an env var or equivalent.

Behold! I’m curling inside a Docker container and from the host and
getting the host’s IP address both times:

``` sh
travis@ip-10–0–8–119:~$ docker exec -t 80dd8ce35ca0 curl http://169.254.169.254/latest/meta-data/local-ipv4; echo
10.0.8.119
travis@ip-10–0–8–119:~$ curl http://169.254.169.254/latest/meta-data/local-ipv4; echo
10.0.8.119
travis@ip-10–0–8–119:~$ echo OMG!
OMG!
```

This is useful for stats and monitoring. So you can track stats by the host,
and have your alerts include the host’s IP so you know exactly where to go to fix your issue.

Aside from the hostname and local IP address, there’s plenty of other metadata:

```
travis@ip-10–0–8–119:~$ curl http://169.254.169.254/latest/meta-data/
ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
hostname
iam/
instance-action
instance-id
instance-type
local-hostname
local-ipv4
mac
metrics/
network/
placement/
profile
public-hostname
public-ipv4
public-keys/
reservation-id
security-groups
```

Let me know on Twitter if you found this post useful.

- [AWS’s documentation on instance metadata](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html)
- [Go lib I wrote to wrap the metadata](https://github.com/travisjeffery/go-ec2-metadata)
