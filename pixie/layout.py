# -*- coding: utf-8 -*-

"""
pixie.layout - Generic code for sorting and laying out sprites
"""


class Sprite(object):
    """
    An image, or similar object, to be packed by Pixie.

    This class is designed to be subclassed by each adapter to provide
    necessary functionality for loading images, querying, trimming and
    generating the resulting atlas.
    """
    def __init__(self, name, width, height):
        self.original_width = self.width = width
        self.original_height = self.height = height
        self.name = name

    @property
    def area(self):
        """
        The area covered by the sprite's bounding rectangle.
        """
        return self.width * self.height

    @property
    def circumference(self):
        """
        The sum of width and height.

        Note that this is not ACTUALLY the circumference!
        """
        return self.width + self.height

    def __repr__(self):
        return "Sprite({name!r}, {width}, {height})".format(**self.__dict__)


class SpritePosition(object):
    """
    A SpritePosition a Sprite positioned for packing.

    This class is used to provide output from the various layout functions.
    """
    def __init__(self, sprite, x, y):
        self.sprite = sprite
        self.x = x
        self.y = y


class Layout(object):
    """
    A Layout instance is returned by the various layout functions. It contains
    all of the information necessary to provide an output bitmap and atlas.
    """
    def __init__(self):
        self.width = 0
        self.height = 0
        self.sprite_positions = []


# Sorting key functions -------------------------------------------------------

def sort_width(r):
    """
    A key function for sorting Sprites by their width attribute.
    """
    return r.width


def sort_height(r):
    """
    A key function for sorting Sprites by their height attribute.
    """
    return r.height


def sort_name(r):
    """
    A key function for sorting Sprites by their name attribute.
    """
    return r.name


def sort_area(r):
    """
    A key function for sorting Sprites by their area property.
    """
    return r.area


def sort_circumference(r):
    """
    A key function for sorting Sprites by their circumference property.
    """
    return r.circumference


def sort_maxside(r):
    """
    A key function for sorting Sprites by the longest of their two sides.
    """
    return max(r.width, r.height)


def sort_sprites(sprites, sort_type):
    """
    A utility function for sorting a list of Sprite instances.

    sort_sprite should be one of 'width', 'height', 'name', 'area',
    'circumference', or 'maxside'
    """
    sort_func = globals()['sort_' + sort_type]
    return sorted(sprites, key=sort_func, reverse=sort_type != 'name')


# Layout functions ------------------------------------------------------------

def layout_horizontal(sprites):
    """
    Return a Layout containing the provided sprites laid out
    linearly horizontally.
    """
    result = Layout()
    for sprite in sprites:
        result.sprite_positions.append(SpritePosition(sprite, result.width, 0))
        result.width += sprite.width
        result.height = max(result.height, sprite.height)
    return result


def layout_vertical(sprites):
    """
    Return a Layout containing the provided sprites laid out
    linearly vertically.
    """
    result = Layout()
    for sprite in sprites:
        result.sprite_positions.append(
            SpritePosition(sprite, 0, result.height))
        result.height += sprite.height
        result.width = max(result.width, sprite.width)
    return result
