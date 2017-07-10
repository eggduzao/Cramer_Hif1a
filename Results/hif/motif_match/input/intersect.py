
import os
import sys

geneFileName = "/home/egg/Projects/Thorsten/Results/motif_match/input/genes+promoters.bed"
openChromFileName = "/home/egg/Projects/Thorsten/Results/open_chromatin/GSM1014183_mm9_wgEncodeUwDnaseLiverC57bl6ME14halfPkRep1.bed"

# Extend
ext = 100
openChromExtFileName = "./temp1.bed"
iff = open(openChromFileName,"r")
off = open(openChromExtFileName,"w")
for line in iff:
  ll = line.strip().split("\t")
  mid = (int(ll[1])+int(ll[2])) / 2
  p1 = mid-ext; p2 = mid+ext
  off.write("\t".join([ll[0],str(p1),str(p2)])+"\n")
iff.close()
off.close()

# Overlap
outFileName = "./open_chromatin.bed"
os.system("intersectBed -a "+openChromExtFileName+" -b "+geneFileName+" -wa -u > "+outFileName)

# Termination
#os.system("rm "+openChromExtFileName)


