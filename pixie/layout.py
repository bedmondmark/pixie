# -*- coding: utf-8 -*-


class Sprite(object):
    def __init__(name, width, height):
        self.width = width
        self.height = height
        self.name = name


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