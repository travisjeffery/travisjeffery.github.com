---
title: "Installing Ruby with rbenv and Homebrew on OS X Mavericks"
date: 2013-06-24T00:00:00Z
tags: ["mac"]
aliases:
  - /b/2013/06/installing-ruby-with-rbenv-and-homebrew-on-os-x-mavericks/
---
It's a bit tricky to install Ruby on Mac OS X Maverick (10.9), but here's what worked for me.

1. Upgrade to Mavericks: https://itunes.apple.com/us/app/os-x-mavericks/id675248567
2. Upgrade to Xcode 5: https://itunes.apple.com/us/app/xcode/id497799835
3. Install the old C compiler to support apps on Ruby 1.8: `brew install apple-gcc42`
4. Let the old compiler know about Xcode 5. Add this to your shell config file in your home directory:

```
# XCode 5 hides these away:
export C_INCLUDE_PATH="$(xcrun --show-sdk-path)/usr/include"
export CPLUS_INCLUDE_PATH="$(xcrun --show-sdk-path)/usr/include"
export LIBRARY_PATH="$(xcrun --show-sdk-path)/usr/lib:$(xcrun --show-sdk-path)/usr/lib/system:$LIBRARY_PATH"
```
