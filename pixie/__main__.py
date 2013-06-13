# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
import sys


if __name__ == '__main__':
    # Hack to allow pixie module to be loaded during development:
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

    from pixie import runner
    runner.main()
