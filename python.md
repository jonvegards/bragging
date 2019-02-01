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

Config of pip:
```
[global]
cert = <path-to-certificate>
trusted-host=
	pypi.python.org
	pypi.org
	files.pythonhosted.org
```
Should be placed in `C:users/username/appdata/roaming/pip`.