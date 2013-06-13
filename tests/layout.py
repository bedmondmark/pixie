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


if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    unittest.main()