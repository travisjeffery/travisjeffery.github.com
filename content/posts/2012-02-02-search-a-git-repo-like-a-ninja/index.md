---
title: "Search a git repo like a ninja"
date: 2012-02-02T00:00:00Z
tags: ["git"]
---
    $ git grep <regexp>

Try it out on a project, then try the same search with ack and grep and you see
that we have speed that's better than either grep or ack. But we can make some
improvements:

- **Allow extended regular expressions**

        $ git config --global grep.extendRegexp true

    git can also support full blown Perl regular expressions as well, by compiling
    git with libpcre. Easy for [homebrew](https://github.com/mxcl/homebrew)
    users:

        $ brew install git --with-pcre

- **Always include line numbers**

        $ git config --global grep.lineNumber true

- **Group output like ack!**

        $ git config --global alias.g "grep --break --heading --line-number"

    As far as I know there is no non-trivial way to add default arguments/override
    git commands, plus g is nice and short.

    Compare this output, without grouping:

    <img class="img-fluid" alt="Without grouping" src="images/without-grouping.jpg" />

    To this much more readable output, with grouping:

    <img class="img-fluid" alt="With grouping" src="images/grouping.jpg" />

    The speed of git grep, which is a product of it being implemented in
    C and only searching your project files, i.e. not files in .git, is
    alone compelling --- but where git grep becomes unique and
    powerful is how it connects you with your repo's git database...

## Practical examples

Here's a list of commands made up of different arguments and concepts of git
grep and git log that you will be able to reuse and learn from to
reformulate later for your own use cases:

- **Search for our regexp in JavaScript files from another branch**

        $ git grep -e <regexp> my_other_branch -- '*.js'

    The `--` signals the end of options and the rest of the paramaters are
    <pathspec> limiters.

- **Search files registered in the index, rather than the working tree**

        $ git grep --cached -e <regexp>

    Note that we're searching what's registered in the index rather than what's staged.

- **Search for staged files containing a regexp that was either added or removed**

        $ git diff-index --cached -G<regexp> HEAD | cut -f2

- **Search through previous revisions whose contents contain a given regexp**

        $ git grep <regexp> $(git rev-list --all)

    I tried the above on one project large enough that git complained about the
    argument size, so if you run into this problem do something like this command:

        $ git rev-list --all | (while read rev; do git grep -e <regexp> $rev; done)

- **Search for commits whose changes include your regexp**

        $ git log -G <regexp>

- **Combine regexps and filter results via boolean logic**

        $ git grep -e 'include' --or 'extend' --and \( -e 'Specification' -e 'Factory' \)

    With this command, we search for lines where we extend *or* include, either specifications *or* factories. For example, let's say we ran this command on this file:

        module UserSpecification; end
        module UserFactory; end
        module Bad; end

        class User
            extend UserSpecification
            include UserFactory
            include Bad
        end

    Then we'd get these results:

    <img class="img-fluid" alt="git grep example" src="images/combination.jpg" />

- **Find files that contain some terms, not necessarily on the same line**

        $ git grep -e <regexp> --and -e <regexp>

    ...is not what you want, as it will search for lines that contain both those
    regular expressions. Instead, this is how we search for files with the matches occurring
    somewhere in the file:

        $ git grep --all-match -e <regexp> -e <regexp>

- **Find commits whose message mention login and were authored by Travis in the last month**

        $ git log --grep=login --author=travis --since=1.month

## Text editor integration

Inevitably we will want to be able to search and use these programs from within
our text editors.

Vim users have it pretty good, with both [ack.vim](https://github.com/mileszs/ack.vim) and Tim
Pope's [Fugitive](https://github.com/tpope/vim-fugitive) which includes `:Ggrep` to interface with
git grep by being to search and have your results listed and linked in the quickfix window. By
listing the results in the quickfix window, you have the usual quickfix navigation keybindings, if
you're unfamiliar, see `:h quickfix`

<img class="img-fluid" alt="Using :Ggrep in Vim" src="images/editor.jpg" />

If your project is not under git version control than you can use ack.vim in a
similar manner:

    :Ack <args>

Emacs user's have had `vc-git-grep` built in since v22.1 and it's very similar
to `:Ggrep`. For acking, use [full-ack](http://www.emacswiki.org/emacs/FullAck).
See [the complation-mode help](http://www.gnu.org/software/emacs/manual/html_node/emacs/Compilation-Mode.html) page (or `C-h f compliation-mode`) for info on navigating in compilation-mode (the mode that both vc-git-grep and full-ack output into).

By now you are comfortable with git grep and git log and you can get more
details on each of these commands by running `git help <command>`. And you have some useful tools in your repertoire --- have fun!

## Sources and further reading

- [Git Tools - Search](https://git-scm.com/book/en/v2/Git-Tools-Searching)
- [Junio C Hamano, current maintainer of git: Fun with "git grep"](http://gitster.livejournal.com/27674.html)
- [Junio C Hamano: Fun with "git log --grep"](http://gitster.livejournal.com/30195.html)
- [How to grep in the git history?](http://stackoverflow.com/questions/2928584/how-to-grep-in-the-git-history)
