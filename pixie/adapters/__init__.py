# -*- coding: utf-8 -*-

from __future__ import absolute_import


def trim_demo():
    "Temporary function - just an experiment."
    from PIL import Image as image

    # Test how image trimming will work:
    im = image.open('tests/data/test.png')
    print im.getbbox()
    im = im.crop(im.getbbox())
    im.show()


# Temporary code:
if __name__ == '__main__':
    trim_demo()
