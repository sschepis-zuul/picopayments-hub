#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2016 Fabian Barkhau <f483@storj.io>
# License: MIT (see LICENSE file)


import sys
from picopayments.main import main


if __name__ == "__main__":
    main(sys.argv[1:])
