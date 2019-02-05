# Emacs:
Useful(?) web pages about Emacs:
- https://www.gnu.org/software/emacs/tour/

## General

| How       | What                    |
|-----------|-------------------------|
| `C-a`     | go to beginning of line |
| `C-a`     | go to end of line       |
| `M-w`     | copy                    |
| `C-w`     | cut                     |
| `C-y`     | paste                   |
| `C-space` | mark text               |
| `C-x b`   | change buffer file      |
| `C-x C-f` | open new/find file      |



## Org-mode

| How         | What                                                     |
|-------------|----------------------------------------------------------|
| `C-c s`     | Write new note                                           |
| `C-x TAB`   | indent marked region with `LEFT, RIGHT, S+LEFT, S+RIGHT` |
| `C-c .`     | Open calendar for setting a timestamp                    |
| `C-c C-x p` | Set a property for a todo-entry                          |
| `C-c C-c`   | Toggle checkbox (cursor at same line as checkbox)        |
| `C-c c t`   | Write a new todo                                         |
|             |                                                          |


## Markdown

| How            | What                                                    |
|----------------|---------------------------------------------------------|
| `C-c S-<DOWN>` | Insert row above in table                               |
| `TAB`          | Jump to next cell, and create new row if at the bottom. |
|                |                                                         |

## Magit

When inside the Magit status windows navigate up and down and press `s` (`u`) for staging (unstaging) files. Press `c` twice to write commit message. `C-c C-c` are used for committing the commit message. Finally use `P u` for pushing the commit to `origin/master`.

| How                        | What                           |
|----------------------------|--------------------------------|
| `C-x g`                    | Magit status frame.            |

| When in Magit status frame |                                 |
|----------------------------|---------------------------------|
| `s`                        | Stage changes at current line.  |
| `c c`                      | Open commit message window.     |
| `C-c C-c`                  | Commit the commit message.      |
| `P u`                      | Push commit to upstream branch. |
|                            |                                 |
