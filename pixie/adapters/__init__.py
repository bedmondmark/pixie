# -*- coding: utf-8 -*-

from __future__ import absolute_import


def trim_demo():
    "Temporary function - just an experiment."
    from PIL import Image as image, ImageChops as imagechops

    # Test how image trimming will work:
    im = image.open('tests/data/Slice 1.png')
    print im.mode, im.size, im.getbbox()
    crop_area = im.split()[3].getbbox()
    return im.crop(crop_area), crop_area


# Temporary code:
if __name__ == '__main__':
    print trim_demo()
