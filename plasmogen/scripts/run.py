
import sys, os
import argparse

from genaf.scripts.run import main as genaf_main, set_config
from rhombus.lib.utils import cout, cerr, cexit

from plasmogen.models.handler import DBHandler


def greet():
    cerr('plasmogen-run - command line utility for plasmogen/genaf/rhombus')


def usage():
    cerr('plasmogen-run - command line utility for plasmogen/genaf/rhombus')
    cerr('usage:')
    cerr('\t%s scriptname [options]' % sys.argv[0])
    sys.exit(0)

print('plasmogen run.py')
set_config( environ='PLASMOGEN_CONFIG',
            paths = ['plasmogen.scripts.'],
            greet = greet,
            usage = usage,
            dbhandler_class = DBHandler
)

def main():
    genaf_main()



