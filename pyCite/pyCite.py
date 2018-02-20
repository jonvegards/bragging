''' Version 1.0.1

*************************************
pyCite -- A Very Useful Python Script
*************************************

Usage:
    >> python3 pycite.py CODE [CODE ... ]

@ Jon Vegard Sparre
'''

# Someone wanted Python 2.X.X-compatibility...
import sys
if sys.version_info[0] < 3: from urllib import urlopen
else: from urllib.request import urlopen
from bs4 import BeautifulSoup
import argparse, string


parser = argparse.ArgumentParser(usage=__doc__)
parser.add_argument('--style', default='bibtex', choices=['bibtex', 'latexUS', 'latexEU'], help='choose style of output (default: bibtex)')
parser.add_argument('codes', nargs='+', help='Codes to search for. Either citation codes or arXiv-codes.')
args = parser.parse_args()

# Dictionary with cmd args and wich module to use
inputCodes  = args.codes
style       = args.style

def inSPIRE_search(searchCode, style):
    prefixes = ['hep-ph', 'hep-th', 'hep-ex', 'HEP-PH', 'HEP-TH', 'HEP-EX']
    if any(x in searchCode for x in prefixes):
        url = "https://inspirehep.net/search?p=" + searchCode
    elif string.punctuation[13] in searchCode or string.punctuation[15] in searchCode:
        url = "https://inspirehep.net/search?p=" + searchCode
    else:
        return("Your search string is invalid: {}".format(searchCode))
    
    try:
        html_doc = urlopen(url).read()
        soup        = BeautifulSoup(html_doc, 'html.parser')
        inspireCode = soup.find(name="abbr").get("title")
        if style == 'bibtex': # BibTeX
            urlBibtex    = "https://inspirehep.net/record/" + inspireCode + "/export/hx"
        elif style == 'latexUS': # LaTeX (US)
            urlBibtex    = "https://inspirehep.net/record/" + inspireCode + "/export/hlxu"
        elif style == 'latexEU': # LaTeX (EU)
            urlBibtex    = "https://inspirehep.net/record/" + inspireCode + "/export/hlxe"
        else: 
            print("Your chosen style is not supported")

        html_doc_bib = urlopen(urlBibtex).read()
        soup_bib         = BeautifulSoup(html_doc_bib, 'html.parser')

        return(soup_bib.find_all(name="div")[4].get_text())
    except:
        return("Sorry, Dave, I can't do that.")

for inputs in inputCodes:
    output = inSPIRE_search(inputs, style)
    print(output)