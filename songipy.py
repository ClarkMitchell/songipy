#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''songipy

Usage:
  songipy ship new <name>...
  songipy ship <name> move <x> <y> [--speed=<kn>]
  songipy ship shoot <x> <y>
  songipy mine (set|remove) <x> <y> [--moored|--drifting]
  songipy -h | --help
  songipy --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
'''

from __future__ import unicode_literals, print_function
from docopt import docopt

__version__ = "0.1.0"
__author__ = "Clark Mitchell"
__license__ = "MIT"


def main():
    '''Main entry point for the songipy CLI.'''
    args = docopt(__doc__, version=__version__)
    print(args)

if __name__ == '__main__':
    main()