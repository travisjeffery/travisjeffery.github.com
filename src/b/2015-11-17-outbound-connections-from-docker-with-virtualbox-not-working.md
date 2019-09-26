---
layout: post.html
title: "Outbound connections from Docker with VirtualBox not working?"
date: 2015-11-17 01:32
comments: false
collection: ops
---

Using Docker and VirtualBox and having trouble making outbound
connections? For instance, you might be getting errors like:

```
curl: (7) Failed connect to 10.0.2.224:8000; No route to host
```

Or:

```
Error: Redis connection to redis:6379 failed - connect EHOSTUNREACH
```

Here's what I did to fix it. First I ssh'd into the Docker machine:

```
$ docker-machine ssh dev
```

And took a look at the network config:

```
$ ifconfig eth0
eth0      Link encap:Ethernet  HWaddr 08:00:27:C8:C7:50
inet addr:10.254.0.15  Bcast:10.254.0.255  Mask:255.255.255.0
inet6 addr: fe80::a00:27ff:fec8:c750/64 Scope:Link
UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
RX packets:230796 errors:0 dropped:0 overruns:0 frame:0
TX packets:62400 errors:0 dropped:0 overruns:0 carrier:0
collisions:0 txqueuelen:1000
RX bytes:238029328 (227.0 MiB)  TX bytes:4768029 (4.5 MiB)
```

Where I see eth0 is configured on this subnet and doesn't seem to be
modifiable. So I fixed this via:

```
$ docker-machine stop dev
$ VBoxManage modifyvm dev --natnet1 "10.254.0.0/24"
$ docker-machine restart dev
```

And boom, just like that it works:

```
$ docker@dev:~$ curl http://10.0.2.224:8000
HTTP/1.1 200 OK
```
