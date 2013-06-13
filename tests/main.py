import os.path
import sys
import unittest


class MainTestCase(unittest.TestCase):
    @property
    def _main(self):
        import pixie.__main__
        return pixie.__main__

    def test_load(self):
        "Ensure pixie.__main__ can be imported"
        main = self._main
        self.assertIsNotNone(main.runner)

if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    unittest.main()