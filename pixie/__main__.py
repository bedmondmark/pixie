# -*- coding: utf-8 -*-

from __future__ import absolute_import

import argparse
import os
import sys


# Hack to allow pixie module to be loaded during development:
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    options = parser.parse_args(argv)

    print options


if __name__ == '__main__':
    main()