Emacs in 2025 and beyond

Next year Emacs turns 50. Pretty impressive for a text editor that's still widely used to this day. I've used Emacs for 25 years now and will probably use it until the day I die. The question is: do use Emacs out of momentum, or if I were new to it today - would I consider it a worthy investment?

Early on when I began programming I did consider other editors. My first ed. I know the upside of Vim. I used Vim for a year or two-ish early on. If life and computers were just about editing text in the fastest way, I would use Vim. On the computer, I write code, run tests, version control, read documentation, shell out (e.g. kubectl, aws cli), calculate math expressions, keep notes, track calendar events, manage accounting, and so on. And Emacs is the only software that does them all, and does them well.

Emacs is aesthetic and thought out, Vim is haphazard. Emacs was designed by Lisp hackers to be a Lisp machine for text. Nearly everything you encounter in Emacs is a Lisp data structures you can inspect and modify. Emacs buffers are sophisticated objects with rich metadata - they have modes - which are just Lisp, local variables, overlays for text properties, and you can programatically manipulate them in Elisp. Emacs' extension language is its implementation language. Whereas, Vim is a C core with Vimscript bolted on top as an afterthought. In Neovim you can use Lua, another bolted on layer on top of the same underlying, awkward API. Vim buffers aren't much more than files in memory. The API for working with them are clunky, relying on ex commands, line operations, and substitions.



Is Emacs still worth using? Absolutely I think. I don't

The two main things I would like in Emacs in the future:

- improved support for async execution for improved responsiveness and consistency, like what Neovim achieved building on libuv. -

Why use Emacs today?

- You can use it for pretty much everything - programming, running terminal commands, writing books, managing your taxes ('m not kidding https://github.com/ledger/ledger-mode). Emacs has LSP and Tree-Sitter support built in. Emacs will be around forever. As the Lindy effect says: the future life expectacy of a non-perisable thing (like a technology or an idea) is proportional to its current age. Emacs isn't the most popular editor. But it's been around forever. It has a healthy following. There is nothing else like it. The core is solid. So it will continue on. Programming LISP is fun and powerful, and I think an ideal environment for building out and customizing something personal like an editor. When working with other people, I prefer boring languages like Go.

Why use Emacs over Vim?

My first few years or so I used Vim, became proficient with the motions, and began writing my own extensions in Vim script. Extending Vim is what motivated me to switch to Emacs.


1. Well architected and extensible. You can make Emacs work how ever you want. This helps future proof it too. Emacs is well thought out and well written. I've used ideas from Emacs in my own programs to make them extensible.

2. Its toolkit is amazing. Org Mode, Magit, Dired, Calc, Projectile, TRAMP, Eshell, Proced where there aren't comperables, if there are comperables, then Emacs outclasses them.

3.

There's a reason why none of the other Emacs implementations never took off in the way that NeoVim took off. Emacs is good, the maintainers will put almost anything good and generally useful into core. But there is no inherit benefit to being in core for LISP code, third-party code has as much power as core code.

There's been other implementations in Rust, and building on Guile.

There are an infinite amount of things I could mention. Emacs really does follow this image when it comes to its learning curve and your skill with it. But to me that makes it even cooler, that I have a tool I'll use my entire life and genueily keep learning the entire time.

Could I write in Vim faster, absolutely. But programminga and writing or doing anything on the computer is more than just writing. You're running tests, running shell commands, managed processes, working with version control, calculating, managing files, and so on. And Emacs can do it all and do it as well as anything.

[^vim]: Aside from first few years using Vim.
[^emacsusers]: Linus Torvalds (technically uemacs, Yukihiro Matsumoto, Donald Knuth, Jamie Zawinski, Richard Stallman (obviously)
[^xemacs]: [XEmacs](https://en.wikipedia.org/wiki/XEmacs).
