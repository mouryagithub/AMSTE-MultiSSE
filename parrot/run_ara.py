#!/usr/bin/env python3
import sys
import ctypes

# Paths to the compiled native extensions
paths = [
    "/mnt/d/Major_Project/parrot/subprojects/ara",
    "/mnt/d/Major_Project/parrot/subprojects/irx",
    "/mnt/d/Major_Project/parrot/build/subprojects/pyllco",
    "/mnt/d/Major_Project/parrot/build/subprojects/ara/ara/steps/native",
    "/mnt/d/Major_Project/parrot/build/subprojects/ara/ara/graph/cgraph",
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
