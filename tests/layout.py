import os.path
import sys
import unittest


class SpriteSortingTestCase(unittest.TestCase):
    @property
    def _layout(self):
        import pixie.layout
        return pixie.layout

    def setUp(self):
        self.wide = self._layout.Sprite('wide', 20, 5)
        self.high = self._layout.Sprite('high', 4, 22)
        self.big = self._layout.Sprite('big', 19, 18)
        self.small = self._layout.Sprite('small', 2, 3)

        self.all = [self.wide, self.high, self.big, self.small]

    def test_sort_width(self):
        layout = self._layout

        self.assertSequenceEqual(
            [self.wide, self.big, self.high, self.small],
            list(layout.sort_sprites(self.all, 'width'))
        )

    def test_sort_height(self):
        layout = self._layout

        self.assertSequenceEqual(
            [self.high, self.big, self.wide, self.small],
            list(layout.sort_sprites(self.all, 'height'))
        )

    def test_sort_area(self):
        layout = self._layout

        self.assertSequenceEqual(
            [self.big, self.wide, self.high, self.small],
            list(layout.sort_sprites(self.all, 'area'))
        )

    def test_sort_circumference(self):
        layout = self._layout

        self.assertSequenceEqual(
            [self.big, self.high, self.wide, self.small],
            list(layout.sort_sprites(self.all, 'circumference'))
        )

    def test_sort_maxside(self):
        layout = self._layout

        self.assertSequenceEqual(
            [self.high, self.wide, self.big, self.small],
            list(layout.sort_sprites(self.all, 'maxside'))
        )

    def test_sort_name(self):
        layout = self._layout

        self.assertSequenceEqual(
            [self.big, self.high, self.small, self.wide],
            list(layout.sort_sprites(self.all, 'name'))
        )


class SpriteTestCase(unittest.TestCase):
    @property
    def _layout(self):
        import pixie.layout
        return pixie.layout

    def test_init(self):
        layout = self._layout

        s = layout.Sprite('jim', 7, 2)
        self.assertEqual('jim', s.name)
        self.assertEqual(7, s.width)
        self.assertEqual(2, s.height)

    def test_area(self):
        layout = self._layout
        s = layout.Sprite('_', 3,4)
        self.assertEqual(12, s.area)

    def test_repr(self):
        layout = self._layout
        s = layout.Sprite('_', 3,4)
        self.assertEqual("Sprite(\'_\', 3, 4)", repr(s))


class SpritePositionTestCase(unittest.TestCase):
    @property
    def _layout(self):
        import pixie.layout
        return pixie.layout

    def test_init(self):
        layout = self._layout
        equal = self.assertEqual

        s = layout.Sprite('jim', 7, 2)
        sp = layout.SpritePosition(s, 0, 0)
        equal(s, sp.sprite)
        equal(0, sp.x)
        equal(0, sp.y)


class LayoutTestCase(unittest.TestCase):
    @property
    def _layout(self):
        import pixie.layout
        return pixie.layout

    def test_init(self):
        layout = self._layout
        equal = self.assertEqual
        l = layout.Layout()
        equal(0, l.width)
        equal(0, l.height)
        equal(0, len(l.sprite_positions))


class layout_TestCase(unittest.TestCase):
    @property
    def _layout(self):
        import pixie.layout
        return pixie.layout

    def test_layout_horizontal(self):
        equal = self.assertEqual
        layout_horizontal = self._layout.layout_horizontal
        Sprite = self._layout.Sprite
        empty = layout_horizontal([])
        equal(0, empty.width)
        equal(0, empty.height)
        equal(0, len(empty.sprite_positions))

        sprite1 = Sprite('a', 12, 24)

        single = layout_horizontal([sprite1])
        equal(12, single.width)
        equal(24, single.height)
        equal(0, single.sprite_positions[0].x)
        equal(0, single.sprite_positions[0].y)
        equal(sprite1, single.sprite_positions[0].sprite)

        sprite2 = Sprite('b', 5, 42)
        sprite3 = Sprite('b', 7, 5)
        triple = layout_horizontal([sprite1, sprite2, sprite3])
        equal(24, triple.width)
        equal(42, triple.height)
        equal(0, triple.sprite_positions[0].x)
        equal(0, triple.sprite_positions[0].y)
        equal(sprite1, triple.sprite_positions[0].sprite)
        equal(12, triple.sprite_positions[1].x)
        equal(0, triple.sprite_positions[1].y)
        equal(sprite2, triple.sprite_positions[1].sprite)
        equal(17, triple.sprite_positions[2].x)
        equal(0, triple.sprite_positions[2].y)
        equal(sprite3, triple.sprite_positions[2].sprite)

    def test_layout_vertical(self):
        equal = self.assertEqual
        layout_vertical = self._layout.layout_vertical
        Sprite = self._layout.Sprite
        empty = layout_vertical([])
        equal(0, empty.width)
        equal(0, empty.height)
        equal(0, len(empty.sprite_positions))

        sprite1 = Sprite('a', 12, 24)

        single = layout_vertical([sprite1])
        equal(12, single.width)
        equal(24, single.height)
        equal(0, single.sprite_positions[0].x)
        equal(0, single.sprite_positions[0].y)
        equal(sprite1, single.sprite_positions[0].sprite)

        sprite2 = Sprite('b', 5, 42)
        sprite3 = Sprite('b', 7, 5)
        triple = layout_vertical([sprite1, sprite2, sprite3])
        equal(12, triple.width)
        equal(71, triple.height)
        equal(0, triple.sprite_positions[0].x)
        equal(0, triple.sprite_positions[0].y)
        equal(sprite1, triple.sprite_positions[0].sprite)
        equal(0, triple.sprite_positions[1].x)
        equal(24, triple.sprite_positions[1].y)
        equal(sprite2, triple.sprite_positions[1].sprite)
        equal(0, triple.sprite_positions[2].x)
        equal(66, triple.sprite_positions[2].y)
        equal(sprite3, triple.sprite_positions[2].sprite)


if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    unittest.main()