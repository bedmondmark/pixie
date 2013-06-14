# -*- coding: utf-8 -*-

"""
pixie.serializers - serializers for storing atlas data in different formats
"""

from __future__ import absolute_import

import json


def _sprite_position_json(sprite_position):
    """
    Convert a SpritePosition to a dict in the correct format for
    TexturePacker output.
    """
    return {
        "filename": sprite_position.sprite.name,
        "frame": {
            "x": sprite_position.x,
            "y": sprite_position.y,
            "w": sprite_position.sprite.width,
            "h": sprite_position.sprite.height
        },
        "rotated": False,
        "trimmed": sprite_position.sprite.trimmed,
        "spriteSourceSize": sprite_position.sprite.sprite_source_size,
        "sourceSize": {
            "w": sprite_position.sprite.original_width,
            "h": sprite_position.sprite.original_height
        }
    }


def json_array(layout):
    """
    Serializer for the TexturePacker json(array) format.
    """
    result = {
        "meta": {
            "app": "https://github.com/bedmondmark/pixie",
            "version": "1.0",
            # "image": "image_file_path.png",
            "format": "RGBA8888",
            "size": {
                "w": layout.width,
                "h":layout.height
            },
            "scale": "1",
        },
        "frames": [
            _sprite_position_json(sprite_position)
            for sprite_position in layout.sprite_positions
        ]
    }
    return json.dumps(result)

