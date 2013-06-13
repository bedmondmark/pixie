import os.path
import sys
import unittest


class RunnerTestCase(unittest.TestCase):
    @property
    def _runner(self):
        import pixie.runner
        return pixie.runner

    def test_parse_args(self):
        runner = self._runner
        options = runner.parse_args([])

if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    unittest.main()