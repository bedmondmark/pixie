import os.path
import sys
import unittest


class PillowAdapterTestCase(unittest.TestCase):
    @property
    def _pillow(self):
        import pixie.adapters.pillow_adapter
        return pixie.adapters.pillow_adapter

    def _data_file(self, path):
        return os.path.join(os.path.dirname(__file__), 'data', path)

    def test_load(self):
        equal = self.assertEqual
        s = self._pillow.load(self._data_file('Slice 1.png'))
        equal(s.width, 203)
        equal(s.height, 203)
        print s.image.getbbox()


if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    unittest.main()