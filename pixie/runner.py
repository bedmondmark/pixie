# -*- coding: utf-8 -*-

"""
pixie.runner - Command-line driver for Pixie
"""

from __future__ import absolute_import

import argparse
import sys

from . import layout
from .adapters import pillow_adapter
from .serializers import json_array


def parse_args(argv):
    """
    Parse argv and return an argparse Namespace.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--sheet')
    parser.add_argument('--data')
    parser.add_argument('images', nargs='+')

    return parser.parse_args(argv)


def main(argv=sys.argv[1:]):
    """
    Entry-point for running the Pixie command-line.
    """
    args = parse_args(argv)
    sprites = [pillow_adapter.load(image_path) for image_path in args.images]
    result = layout.layout_horizontal(sprites)
    print json_array(result)