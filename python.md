# iPython/Python related commands

Profiling functions/commands in Python.
```python
>> %prun <command>
   profiling <command>
```

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