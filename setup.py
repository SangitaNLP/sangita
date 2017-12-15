#!/usr/bin/env python3


import sys
from setuptools import setup


if sys.argv[-1] == 'setup.py':
    print('To install, run \'python setup.py install\'')
    print()

if sys.version_info[:2] < (3, 5):
    print(('lingatagger requires Python version 3.5 or later (%d.%d detected).' %sys.version_info[:2]))
    sys.exit(-1)
    
    
if __name__ == "__main__":
    setup(
        name = 'Sangita',
        version = '1.0',
        author = 'Samrridhi Sinha',
        author_email = 'samridhhisinha.iitkgp@gmail.com',
        description = 'A Natural Language Toolkit for Indian Languages', 
        url = 'https://github.com/djokester/sangita'
        keywords = ['nlp', 'hindi', 'linguistics'],
        packages = ['sangita.hindi', 'sangita.hindi.corpora'],
        license = 'Apache License'
    )
