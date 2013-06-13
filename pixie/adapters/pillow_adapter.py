# -*- coding: utf-8 -*-

"""
pixie.adapters.pillow_adapter - Adapter that uses pillow for image manipulation
"""

from __future__ import absolute_import

from PIL import Image as image

from ..layout import Sprite


class PillowSprite(Sprite):
    def __init__(self, path):
        self.path = path
        self.image = image.open(path)
        self.width = self.image.size[0]
        self.height = self.image.size[1]
        self.trimmed = False
        self.trim_offsets = None
        self.original_width = self.width
        self.original_height = self.height

    def trim(self):
        if not self.trimmed:
            self.image, off = _trim(self.image)
            if off:
                self.trimmed = True
                self.original_width = self.width
                self.original_height = self.height
                self.width = off[2] - off[0]
                self.height = off[3] - off[1]
                self.trim_offsets = off


def _trim(im):
    channels = im.split()
    if len(channels) != 4:
        return im, None
    crop_area = channels[3].getbbox()
    return im.crop(crop_area), crop_area


def load(path):
    return PillowSprite(path)