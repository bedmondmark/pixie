# -*- coding: utf-8 -*-


class Sprite(object):
    def __init__(self, name, width, height):
        self.width = width
        self.height = height
        self.name = name

    @property
    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "Sprite({name!r}, {width}, {height})".format(**self.__dict__)


class SpritePosition(object):
    def __init__(self, sprite, x, y):
        self.sprite = sprite
        self.x = x
        self.y = y


class Layout(object):
    def __init__(self):
        self.width = 0
        self.height = 0
        self.sprite_positions = []


# Sorting key functions -------------------------------------------------------

def sort_width(r):
    return r.width


def sort_height(r):
    return r.height


def sort_name(r):
    return r.name


def sort_area(r):
    return r.width * r.height


def sort_circumference(r):
    return r.width + r.height


def sort_maxside(r):
    return max(r.width, r.height)


def sort_sprites(sprites, sort_name):
    sort_func = globals()['sort_'+sort_name]
    return sorted(sprites, key=sort_func, reverse=sort_name != 'name')


# Layout functions ------------------------------------------------------------

def layout_horizontal(sprites):
    result = Layout()
    for sprite in sprites:
        result.sprite_positions.append(SpritePosition(sprite, result.width, 0))
        result.width += sprite.width
        result.height = max(result.height, sprite.height)
    return result


def layout_vertical(sprites):
    result = Layout()
    for sprite in sprites:
        result.sprite_positions.append(SpritePosition(sprite, 0, result.height))
        result.height += sprite.height
        result.width = max(result.width, sprite.width)
    return result

