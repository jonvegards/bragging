# Commands that are handy to remember

## Emacs:
```
C-a	go to beginning of line
C-a	go to end of line
M-w	copy
C-w cut
C-y	paste
C-space mark text
C-x b	change buffer file
C-x C-f	open new/find file
```

## Terminal
```
>> file <filename>
	prints out which type of file it is

>> tail -n <number>
	show the <number> last lines of sth

>> head -n <number>
	show the <number> first lines of sth

		Example:
			>> ls -l | head -n 1
				show the first line of what the command ls -l prints out

>> ls path/to/folder | wc -l
	gives number of files in that folder. 'wc' counts every line of the
	output to 'ls -l' so remember to subtract 1.

>> man <sth>
	show the manual to a command

>> scp jonvsp@abel.uio.no:~/path/to/file path/on/local/machine
	copy a file from somewhere (e.g. Abel) to folder on your own computer
	when it's connected to UiO's network

>> diff file1 file2
	gives you the lines that are different in each file, e.g.
	< something something 			# this is in file1
	> something something			# this is in file2

>> du -sh path/to/folder_or_file
	gives the size of the chosen folder or file in a human readable format (s is 
	summarizing all subfolders and files to one number)

>> lscpu
	get info about CPU

>> less <file>
	show file content in terminal

>> ls -l <file or directory> | wc -l
	count lines of file/number of files in directory

>> find . -type f -name "<filename>"
   	search for files in current directory, change <.> with name of directory you want to search in

>> grep 'word' filename1 [filename2 ...]
    search for 'word' in filename1 [filename2 ...]
    options: --color : highlights the search word)
             -n      : print the line number where search word was found
             -v      : invert the match, print lines that do not contain search word
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
```