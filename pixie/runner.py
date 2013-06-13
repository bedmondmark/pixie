# -*- coding: utf-8 -*-

"""
pixie.runner - Command-line driver for Pixie
"""

from __future__ import absolute_import

import argparse
import sys


def parse_args(argv):
    parser = argparse.ArgumentParser()

    return parser.parse_args(argv)


def main(argv=sys.argv[1:]):
    print parse_args(argv)