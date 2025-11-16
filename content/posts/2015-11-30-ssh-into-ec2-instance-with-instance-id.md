---
title: "SSH into EC2 instance with instance ID"
date: 2015-11-30T00:00:00Z
tags: ["ops"]
---
Make sure you've installed and configured the [aws-cli](https://github.com/aws/aws-cli) and [jq](https://github.com/stedolan/jq).

Drop this function into your .zshrc or .bashrc:

``` sh
function ec2-ssh () {
  ssh $(aws ec2 describe-instances --filter Name=instance-id,Values=$1 | jq '.Reservations[0].Instances[0].PrivateIpAddress' | tr -d '"')
}
```

And now you can ssh into your EC2 instance:

``` sh
$ ec2-ssh i-6g5c7ed4
```
