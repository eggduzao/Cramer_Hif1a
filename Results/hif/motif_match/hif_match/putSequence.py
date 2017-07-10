
import os
import sys

inocn = "/home/egg/Projects/Cramer/Results/motif_match/Match/open_chromatin_mpbs.bed"
inpn = "/home/egg/Projects/Cramer/Results/motif_match/Match/promoter_mpbs.bed"
outocn = "/home/egg/Projects/Cramer/Results/motif_match/Match/open_chromatin_hif1a.bed"
outpn = "/home/egg/Projects/Cramer/Results/motif_match/Match/promoter_hif1a.bed"
genome = "/home/egg/rgtdata/mm9/genome_mm9.fa"

ofc = "t1.fa"
ofp = "t2.fa"
os.system("bedtools getfasta -fi "+genome+" -bed "+inocn+" -fo "+ofc)
os.system("bedtools getfasta -fi "+genome+" -bed "+inpn+" -fo "+ofp)

fastaFile = open(ofc,"r")
mpbsFile = open(inocn,"r")
outFile = open(outocn,"w")
for line in mpbsFile:
  ll = line.strip().split("\t")
  fastaFile.readline()
  seq = fastaFile.readline().strip().upper()
  outFile.write("\t".join(ll+[seq])+"\n")
fastaFile.close()
mpbsFile.close()
outFile.close()

fastaFile = open(ofp,"r")
mpbsFile = open(inpn,"r")
outFile = open(outpn,"w")
for line in mpbsFile:
  ll = line.strip().split("\t")
  fastaFile.readline()
  seq = fastaFile.readline().strip().upper()
  outFile.write("\t".join(ll+[seq])+"\n")
fastaFile.close()
mpbsFile.close()
outFile.close()

os.system("rm "+ofc+" "+ofp)


