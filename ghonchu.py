#!/usr/bin/env python
"""ghonchu.py: 

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
from core import globals
from core import execute

def run(conf, args):
    globals.conf = conf
    if args.new_note:
        print("Writing a new note")
    elif args.update_note:
        print("Updating a new note")

def main():
    import argparse
    # Argument parser.
    description = '''A stupid personal manager'''
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--config', '-c', metavar='config_file'
            , default = os.path.join(os.environ["HOME"], ".ghonchurc")
            , help = 'Configuration file.'
            )

    sp = parser.add_mutually_exclusive_group()
    sp.add_argument('--new-note', '-nn'
            , default = ""
            , type = str
            , help = 'Write a new note'
            )
    sp.add_argument('--update-note', '-un'
            , type = str
            , default = ''
            , help = 'Update an old note'
            )

    class Args: pass 
    args = Args()
    parser.parse_args(namespace=args)
    try:
        import ConfigParser as cfg
    except:
        import configparser as cfg

    conf = cfg.ConfigParser()
    conf.readfp(open(args.config))
    run(conf, args)

if __name__ == '__main__':
    main()
