#!/usr/bin/env python
import os
import sys

# Find locuszoom binary. 
sys.argv[0] = os.path.abspath(sys.argv[0]);
lzbin = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]),"../bin/locuszoom"));

# Run a quick example  
cmd = "%(bin)s --metal epistasis_bodyfat_8wks_male.txt --chr 7 --start 98199548 --end 100258155 --ld-vcf snp142.vcf.gz" % {'bin' : lzbin};
print "Running: %s" % cmd;
os.system(cmd); 
