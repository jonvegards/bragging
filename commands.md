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