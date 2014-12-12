"""note.py: 
    
    Note class.

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

import sys
import tempfile
import os
import subprocess
from core import globals

class Note(object):
    """docstring for Note"""
    def __init__(self, title):
        super(Note, self).__init__()
        self.title = title
        self.editor = "vim"
        self.notefile = tempfile.NamedTemporaryFile(suffix=".tmp")
        self.notedir = globals.config_.get('global', 'path')
        if not os.path.isdir(self.notedir):
            os.makedirs(self.notedir)

        self.filepath = os.path.join(self.notedir, self.title)

        if globals.config_.get('global', 'editor', None) is None:
            print("++ Setup EDITOR environment variable or live with vim")
            self.editor = globals.editor_

    def write(self, **kwargs):
        print("Writing a note with title: %s" % self.title)
        self.notefile.write(self.title)
        with open(self.filepath, "a+") as f:
            subprocess.call([self.editor, f.name])

        
