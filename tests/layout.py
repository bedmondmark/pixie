import os.path
import sys
import unittest


class DefaultLayoutTestCase(unittest.TestCase):
    @property
    def _layout(self):
        import pixie.layout
        return pixie.layout

    def test_layout(self):
        layout = self._layout
        self.fail("This test is not finished yet!")


if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    unittest.main()