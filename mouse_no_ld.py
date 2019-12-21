#!/usr/bin/env python
import os
import sys

# Find locuszoom binary. 
sys.argv[0] = os.path.abspath(sys.argv[0]);
lzbin = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]),"../bin/locuszoom"));

# Run a quick example  
cmd = "%(bin)s --metal epistasis_bodyfat_8wks_male.txt --chr 1 --start 5000000 --end 6000000 --no-ld" % {'bin' : lzbin};
print "Running: %s" % cmd;
os.system(cmd); 
