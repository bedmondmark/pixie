# -*- coding: utf-8 -*-

import os
import sys

# Hack to allow pixie module to be loaded during development:
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pixie import main

main()