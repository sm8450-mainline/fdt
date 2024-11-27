import os
import sys

sys.path.insert(0, os.getcwd())

from pyfdt.pyfdt import FdtBlobParse, FdtProperty

with open(sys.argv[1], "rb") as infile:
    dtb = FdtBlobParse(infile)
    fdt = dtb.to_fdt()

print(fdt.to_dts())
