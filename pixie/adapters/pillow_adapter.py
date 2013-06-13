# -*- coding: utf-8 -*-

"""
pixie.adapters.pillow_adapter - Adapter that uses pillow for image manipulation
"""

from __future__ import absolute_import

from PIL import Image as image

from ..layout import Sprite


class PillowSprite(Sprite):
    """
    A pillow-specific subclass of Sprite.

    On instantiation, this class will load the image at `path` and inspect the
    image data in order to populate the various Sprite attributes.
    """
    def __init__(self, path):
        self.path = path
        self.image = image.open(path)
        width = self.image.size[0]
        height = self.image.size[1]
        super(PillowSprite, self).__init__(path, width, height)

    @property
    def trimmed(self):
        """
        A boolean, indicating whether this Sprite has been trimmed or not.
        """
        return self.trim_offsets is not None

    def trim(self):
        """
        Attempt to trim the image encapsulated by this Sprite.
        """
        if not self.trimmed:
            self.image, off = _trim(self.image)
            if off:
                self.original_width = self.width
                self.original_height = self.height
                self.width = off[2] - off[0]
                self.height = off[3] - off[1]
                self.trim_offsets = off


def _trim(original):
    """
    Trim the provided image `original`.

    This function returns a 2-tuple containing the cropped image and the
    (x, y, w, h) tuple of the cropped area, or None if the image could not
    be trimmed.
    """
    channels = original.split()
    if len(channels) != 4:
        return original, None
    crop_area = channels[3].getbbox()
    return original.crop(crop_area), crop_area


def load(path):
    """
    Load the image at `path` and return a Sprite representing the loaded image.
    """
    return PillowSprite(path)
