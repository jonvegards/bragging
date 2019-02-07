# Jupyter iPython/Python related commands

Profiling functions/commands in Python.
```python
>> %prun <command>
   profiling <command>
```

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

# General `Python`
Silence warnings
```python
>> import warnings
>> warnings.filterwarnings("ignore")
   silence warnings
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

When using jupyter it's possible to do the programming in an IDE while you run the code in jupyter, see
https://medium.com/@rrfd/cookiecutter-data-science-organize-your-projects-atom-and-jupyter-2be7862f487e
By using
```python
%load_ext autoreload
%autoreload 2
```
Jupyter will reload the module everytime before running the code.
