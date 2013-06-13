# -*- coding: utf-8 -*-

from __future__ import absolute_import

import argparse
import sys


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()

    options = parser.parse_args(argv)

    print options