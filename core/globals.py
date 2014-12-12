
"""globals.py: Keep your globals here.

Last modified: Sat Jan 18, 2014  05:01PM

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2013, Dilawar Singh and NCBS Bangalore"
__credits__          = ["NCBS Bangalore"]
__license__          = "GNU GPL"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import os 
import time
import datetime

st = time.time()

stamp_ = datetime.datetime.fromtimestamp(st).strftime('%Y-%m-%d-%H%M')

config_ = None
editor_ = os.environ.get('EDITOR', 'vim')
