# -*- coding: utf-8 -*-

from __future__ import absolute_import

from PIL import Image as image

from ..layout import Sprite


class PillowSprite(Sprite):
    def __init__(self, path):
        self.path = path
        self.image = image.open(path)
        self.width = self.image.size[0]
        self.height = self.image.size[1]


def load(path):
    return PillowSprite(path)