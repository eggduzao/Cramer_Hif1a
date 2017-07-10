
import os
import sys

window = 500
sw = 10

#inFileName = "/home/egg/Projects/Cramer/Results/motif_match/input/genes.bed"
#outFileName = "/home/egg/Projects/Cramer/Results/motif_match/input/promoters.bed"
inFileName = "/home/egg/rgtdata/mm9/genes_mm9.bed"
outFileName = "/home/egg/Projects/Thorsten/Results/motif_match/input/all_mm9_promoters.bed"
inFile = open(inFileName,"r")
outFile = open(outFileName,"w")
for line in inFile:
  ll = line.strip().split("\t")
  if(ll[5] == "+"):
    p2 = int(ll[1]) + sw
    p1 = p2 - window - sw
  else:
    p1 = int(ll[2]) - sw
    p2 = p1 + window + sw
  outFile.write("\t".join([ll[0],str(p1),str(p2),ll[3]+"_promoter"])+"\n")
inFile.close()
outFile.close()


