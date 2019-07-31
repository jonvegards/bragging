# Commands that are handy to remember

About versioning code: https://semver.org

## Terminal
```
>> diff file1 file2
	gives you the lines that are different in each file, e.g.
	< something something 			# this is in file1
	> something something			# this is in file2

>> disown -h %1
	detach job number 1 from terminal, then use 'bg 1' to set the job running
	in the background and you're able to disconnect (SSH) without killing the
	job.

>> du -sh path/to/folder_or_file
	gives the size of the chosen folder or file in a human readable format (s is 
	summarizing all subfolders and files to one number)

>> file <filename>
	prints out which type of file it is

>> find folder2 -name '*.*' | xargs mv --target-directory=folder1
    move all files from folder2 to folder1

>> find . -type f -name "<filename>"
   	search for files in current directory, change <.> with name of directory you want to search in

>> grep 'word' filename1 [filename2 ...]
    search for 'word' in filename1 [filename2 ...]
    options: --color : highlights the search word)
             -n      : print the line number where search word was found
             -v      : invert the match, print lines that do not contain search word

>> head -n <number>
	show the <number> first lines of sth

		Example:
			>> ls -l | head -n 1
				show the first line of what the command ls -l prints out

>> less <file>
	show content of <file> in terminal

>> ls path/to/folder | wc -l
	gives number of files in that folder. 'wc' counts every line of the
	output to 'ls -l' so remember to subtract 1.

>> lscpu
	get info about CPU

>> ls -l <file or directory> | wc -l
	count lines of file/number of files in directory

>> man <sth>
	show the manual to a command

>> scp jonvsp@abel.uio.no:~/path/to/file path/on/local/machine
	copy a file from somewhere (e.g. Abel) to folder on your own computer
	when it's connected to UiO's network

>> tail -n <number>
	show the <number> last lines of sth
	
>> for i in $files; do sed 1d "$i" >> <new-file>; done
	merge all files listed in $files into one new file.

```

## GitHub:
```
>> git add .
   add all new/changed files to the Git queue
>> git commit -am '<commit message here>'
   Open Emacs for adding a comment on changes
>> git push
   Push the new/edited files to git
>> git pull
   Downloads new/edited files from git to computer
>> git filter-branch --force --index-filter "git rm --cached --ignore-unmatch <path/filename>" --prune-empty --tag-name-filter cat -- --all
   Remove file from history, useful when you add files larger than 100MB by accident.
>> git config --list --show-origin
   Show where config-files for git are saved.
```

## Abel:
```
>> beegfs-ctl --userstats --names --mount=<mount>
   view the file writing load on --mount=/work or --mount=/cluster

>> sbatch job_script
   start new job with job script

>> squeue -l -u [username]
   view all your jobs running/pending

>> scontrol show job [job id number]
   info about your job

>> scancel [job id number]
   kill job

>> qsumm -g
   view workload on Abel
```

# Markdown

## Including stuff in markdown-file

| What   | How                   | Comment                                       |
|--------|-----------------------|-----------------------------------------------|
| Images | `![](<url-to-image>)` | afaik relative refs inside repo does not work |
|        |                       |                                               |


# Emacs:
Useful(?) web pages about Emacs:
- https://www.gnu.org/software/emacs/tour/

## General

| How       | What                                                                            |
|-----------|---------------------------------------------------------------------------------|
| `C-a`     | go to beginning of line                                                         |
| `C-a`     | go to end of line                                                               |
| `M-w`     | copy                                                                            |
| `C-w`     | cut                                                                             |
| `C-y`     | paste                                                                           |
| `C-space` | mark text                                                                       |
| `C-x b`   | change buffer file                                                              |
| `C-x C-f` | open new/find file                                                              |
| `C-c m c` | use multiple cursors (you must mark a region in the file before using this cmd) |
| `C-x o`   | Select other window.                                                            |
| `C-v`     | View next screen (scroll down)                                                  |
| `M-V`     | View previous screen (scroll up)                                                |
|           |                                                                                 |

## Org-mode

| How         | What                                                     |
|-------------|----------------------------------------------------------|
| `C-c c`     | Write new note                                           |
| `C-x TAB`   | indent marked region with `LEFT, RIGHT, S+LEFT, S+RIGHT` |
| `C-c .`     | Open calendar for setting a timestamp                    |
| `C-c C-x p` | Set a property for a todo-entry                          |
| `C-c C-c`   | Toggle checkbox (cursor at same line as checkbox)        |
| `C-c c t`   | Write a new todo                                         |
| `C-u C-c`   | Create timestamp                                         |
| `C-c s`     | Schedule a todo entry                                    |
| `C-c d`     | Set a deadline for a todo entry                          |
| `C-c C-e`   | Export-mode window is opened                             |

Docs: https://orgmode.org/org.html

## Markdown

| How            | What                                                    |
|----------------|---------------------------------------------------------|
| `C-c S-<DOWN>` | Insert row above in table                               |
| `TAB`          | Jump to next cell, and create new row if at the bottom. |
| `C-c C-s c`    | Insert code                                             |
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

Docs: https://magit.vc/manual/magit.html

## Miscellaneous links and info
- http://pragmaticemacs.com/emacs/multiple-cursors/

# Powershell

| Cmd           | What it does            |
|---------------|-------------------------|
| `Get-Command` | List all available cmds |
|               |                         |

# Jupyter/iPython/Python

## Profiling
Profiling functions/commands in Python.
```python
>> %prun <command>
   profiling <command>
```

In `iPython` you can use bash-cmds as `ls`, `pwd`, ...

## Keyboard shortcuts in Jupyter
| Cmd           | Description                        |
|---------------|------------------------------------|
| `Enter`       | enter edit mode                    |
| `Shift­Enter` | run cell, select below             |
| `Ctrl-Enter`  | run cell                           |
| `Alt-Enter`   | run cell, insert below             |
| `Y`           | to code                            |
| `M`           | to markdown                        |
| `R`           | to raw                             |
| `1`           | to heading 1,2,3,4,5,6             |
| `Up/K`        | select cell above                  |
| `Down/J`      | select cell below                  |
| `A/B`         | insert cell above/­below           |
| `X`           | cut selected cell                  |
| `C`           | copy selected cell                 |
| `Shift-V`     | paste cell above                   |
| `V`           | paste cell below                   |
| `Z`           | undo last cell deletion            |
| `D,D`         | delete selected cell               |
| `Shift-M`     | merge cell below                   |
| `Ctrl-S`      | Save and Checkpoint                |
| `L`           | toggle line numbers                |
| `O`           | toggle output                      |
| `Shift-O`     | toggle output scrolling            |
| `Esc`         | close pager                        |
| `H`           | show keyboard shortcut help dialog |
| `I,I`         | interrupt kernel                   |
| `0,0`         | restart kernel                     |
| `Space`       | scroll down                        |
| `Shift­Space` | scroll up                          |
| `Shift`       | ignore                             |

When using jupyter it's possible to do the programming in an IDE while you run the code in jupyter, see
https://medium.com/@rrfd/cookiecutter-data-science-organize-your-projects-atom-and-jupyter-2be7862f487e
By using
```python
%load_ext autoreload
%autoreload 2
```
Jupyter will reload the module everytime before running the code.

### R in Jupyter
Assuming `python`, `jupyter`, and `R`  are installed with `brew`, the way to gey `R` into `jupyter notebook` is to run
```bash
>> brew install zmq
```
And then open `R` and install
```r
install.packages(c('rzmq','repr','IRkernel','IRdisplay'),
                 repos = c('http://irkernel.github.io/', 
                           getOption('repos')), 
                 type = 'source')
IRkernel::installspec(user = FALSE)
```

### Links to stuff about Jupyter
- https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/
- https://towardsdatascience.com/optimizing-jupyter-notebook-tips-tricks-and-nbextensions-26d75d502663

# General `Python`
Silence warnings
```python
import warnings
warnings.filterwarnings("ignore")
```

Config of pip with `pip.ini` file:
```
[global]
cert = <path-to-certificate>
trusted-host=
	pypi.python.org
	pypi.org
	files.pythonhosted.org
```
Should be placed in `C:users/username/appdata/roaming/pip`.

Build setuptools project:
```
python setup.py sdist bdist_wheel
```

Generate a virtual environment
```
python3 -m venv /path/to/new/virtual/environment
```

Read `7z`-files (@ Engel 1)
```
cmd = r'C:\\Program Files\\7-Zip\\7z.exe x -y -p<password>  <filename>.7z'
file = subprocess.call(shlex.split(cmd))
```
(`-y` = assume yes on all queries.)

# R

## Basic commands

| Cmd                                 | What                                                        |
|-------------------------------------|-------------------------------------------------------------|
| `setwd('')`                         | Change directory                                            |
| `getwd('')`                         | Get current directory                                       |
| `library('<bibliotek>')`            | Load library                                                |
| `colnames(<dataframe>)`             | Print name of columns in dataframe                          |
| `factors <- sapply(ods, is.factor)` | Return a boolean array indicating categorical data in `ods` |
| `system.time()`                     | Time execution of function/script                           |

- Lage en liste: `vars_cat = c('val', 'val2', ...)`
- Konverterer kolonnene `vars_cat` i datasettet `ods` til kategoriske variable: `ods[vars_cat] <- lapply(ods[vars_cat], as.factor)`

## Installing packages

Set an option before installing: `options(download.file.method = "libcurl")`

Install-cmd: `install.packages("<package>", repos="https://nexus-r.adeo.no/repository/cran.r-project.org/")`
