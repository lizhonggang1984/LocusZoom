# LocusZoom

# download required software and intalled in Linux environment
https://genome.sph.umich.edu/wiki/LocusZoom_Standalone

(1) install python and R in linux system
(2) install new_fugue  and  plink for LD calculation
(3) download the full folder of locuszoom (including all data files with LD files) to drive, untar all files

# In Attie-VM, all software has been installed

# Our Locuszoom is in attie-vm at :
/mnt/data/locuszoom

# To use mouse data, follow next steps
(1)go the example folder 
(2) use the Python script for analysis.
If change the path, go to conf folder and change the configure file.

we already updated mm10 to .db:
bin/lzupdate.py --build mm10 

using conf/m2z.config file to change your configuration

# To run LocusZoom to draw mouse genome locuszoom, use six steps:

(1) log in into Attie-VM
(2)$ ls
   $ sudo su
   $ (YOURpassword)
   $ cd /mnt/data/locuszoom/examples
(3) // conduct shell to setup path for tabix for LD calculation 
   export PATH=$PATH:/mnt/data/locuszoom/tabix-0.2.6

(4) //upload gwas file to the example folder

   this text file must have at least two columns,   
   MarkerName and P-value (column name should be exactly these two)
   
(5) // edit python file to perform locuszoom
   // to calculate LD, using mouse_vcf.py to do it
   
   change   --refsnp  to your snp  and change --flank   to 200kb or 500kb as needed
   
(6)  //conduct  ./mouse_vcf.py to draw plots

   ./mouse_vcf.py
   
