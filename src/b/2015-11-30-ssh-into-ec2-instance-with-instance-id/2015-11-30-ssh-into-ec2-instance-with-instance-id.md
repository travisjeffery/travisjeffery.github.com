---
layout: post.html
title: "SSH into EC2 Instances By Instance Id"
date: 2015-11-30 22:05
comments: true
categories: ec2 aws
---

Make sure you've got the [aws-cli](https://github.com/aws/aws-cl) and [jq](https://github.com/stedolan/jq) installed and configured.

Drop this into your .zshrc or .bashrc:

``` sh
function ec2-ssh () {
  ssh $(aws ec2 describe-instances --filter Name=instance-id,Values=$1 | jq '.Reservations[0].Instances[0].PrivateIpAddress' | tr -d '"')
}
```

And now you can ssh into your EC2 instance with:

``` sh
ec2-ssh i-6g5c7ed4
```
