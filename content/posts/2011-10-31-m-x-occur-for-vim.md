---
title: "M-x occur for Vim"
date: 2011-10-31T00:00:00Z
tags: ["vim"]
aliases:
  - /b/2011/10/m-x-occur-for-vim/
---
Emacs has a feature named "occur" that lists the lines in the current buffer that match a given regexp. I've created the equivalent feature in Vim:

```
nmap g/ :vimgrep /<C-R>//j %<CR>\|:cw<CR>
```

With this mapped, here's how you'd use it:

1. Search for you're looking for with `/my query<CR>`.
2. Press `g/` to open the quickfix list containing the matched lines.
3. Navigate to the line you're interested in and press `<CR>`.
   
You could create a function to combine the steps; taking the query as input, running the search, and
opening the quickfix list. But I prefer having them separate.
