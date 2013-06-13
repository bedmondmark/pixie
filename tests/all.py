#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os.path
import sys
import unittest

if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

    from layout import *
    from pillow_adapter import *

    unittest.main()