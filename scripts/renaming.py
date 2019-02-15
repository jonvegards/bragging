"""
Script for renaming files.

Example:
Your folder is full of these files:

abc_2000.jpg
abc_2001.jpg
abc_2004.jpg
abc_2007.jpg

Which you want to rename into:

year_2000.jpg
year_2001.jpg
year_2004.jpg
year_2007.jpg

To do this, run:
>>> python renaming.py -s _ -c abc

Made with inspiration from:
https://stackoverflow.com/questions/17748228/rename-multiple-files-in-python
"""

import os
import glob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--split", help="characters to split on", type=str)
parser.add_argument("-c", "--common-name", help="common words/characters in paths to be renamed", type=str)
args = parser.parse_args()


files = glob.glob(args.common_name)
for file in files:
    os.rename(file, '{}'.format(file.split(args.split)[1]))
