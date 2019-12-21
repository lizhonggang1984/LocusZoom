#!/usr/bin/env python
import os
import sys

# Find locuszoom binary. 
sys.argv[0] = os.path.abspath(sys.argv[0]);
lzbin = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]),"../bin/locuszoom"));

# Run a quick example from the Kathiresan et al. data. 
cmd = "%(bin)s --metal ./glgc/ldl.txt --refgene SESN1 --flank 200kb" % {'bin' : lzbin};
print "Running: %s" % cmd;
os.system(cmd); 
