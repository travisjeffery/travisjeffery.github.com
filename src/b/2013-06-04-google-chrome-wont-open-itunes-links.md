---
layout: post.html
title: "When Google Chrome won't open iTunes links"
date: 2013-06-04 19:54
comments: true
collection: googlechrome
---

Recently ran into this issue where Google Chrome wouldn't open iTunes links
(e.g. links to WWDC videos, iOS apps, songs, etc.), a while
ago I'd set Chrome to remember not open those links (oops).

Rather than blowing away all your settings in Chrome, here's the fix:

1. Open up this file `~/Library/Application Support/Google/Chrome/Local State`
2. Find the line containing either `itms` or `itmss` and delete it. The line will be something like: `"itms": true,`.
3. Quit and reopen Chrome
4. Wa-Lah!
