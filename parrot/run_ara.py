#!/usr/bin/env python3
import os
import sys
import ctypes

base = os.path.dirname(os.path.abspath(__file__))

# Paths to the compiled native extensions
paths = [
    os.path.join(base, "subprojects/ara"),
    os.path.join(base, "subprojects/irx"),
    os.path.join(base, "build/subprojects/pyllco"),
    os.path.join(base, "build/subprojects/ara/ara/steps/native"),
    os.path.join(base, "build/subprojects/ara/ara/graph/cgraph"),
]

for p in paths:
    if p not in sys.path:
        sys.path.insert(0, p)

# Load pyllco with RTLD_GLOBAL so its symbols are exported to graph_data
sys.setdlopenflags(sys.getdlopenflags() | ctypes.RTLD_GLOBAL)
import pyllco

from ara.ara import Main
main = Main()
sys.exit(main.main())

