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
        self.assertFalse(s.trimmed)
        equal(s.width, 203)
        equal(s.height, 203)

    def test_trim(self):
        equal = self.assertEqual
        s = self._pillow.load(self._data_file('Slice 1.png'))
        s.trim()
        self.assertTrue(s.trimmed)
        equal(s.width, 120)
        equal(s.height, 120)
        equal(s.original_width, 203)
        equal(s.original_height, 203)
        equal(s.trim_offsets, (41, 41, 161, 161))

        # Ensure it doesn't mess up trimming twice:
        s.trim()
        self.assertTrue(s.trimmed)
        equal(s.width, 120)
        equal(s.height, 120)
        equal(s.original_width, 203)
        equal(s.original_height, 203)
        equal(s.trim_offsets, (41, 41, 161, 161))

        # Test with an opaque image:
        s = self._pillow.load(self._data_file('opaque.jpg'))
        self.assertFalse(s.trimmed)
        equal(s.width, 554)
        equal(s.height, 422)
        s.trim()
        equal(s.width, 554)
        equal(s.height, 422)


if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    unittest.main()