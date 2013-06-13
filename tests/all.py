#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os.path
import sys
import unittest

if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

    from test_layout import *
    from test_pillow_adapter import *
    from test_main import *
    from test_runner import *

    unittest.main()