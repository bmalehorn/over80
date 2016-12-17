#!/usr/bin/env python3

# Somewhere, a Python developer cries a single tear at the simplicity of this
# script.

import sys

for f in sys.argv[1:]:
    for line_number, line in enumerate(open(f).read().splitlines(), start=1):
        if len(line) > 80:
            print("%s:%d:%s" % (f, line_number, line))
