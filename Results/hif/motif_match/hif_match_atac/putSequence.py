
import os
import sys

inocn = "/home/egg/Projects/Thorsten/Results/thorsten/hif/motif_match/hif_match_atac/atac_hif1a_genes.bed"
outocn = "/home/egg/Projects/Thorsten/Results/thorsten/hif/motif_match/hif_match_atac/atac_hif1a_genes_motifseq.bed"
genome = "/home/egg/rgtdata/mm9/genome_mm9.fa"

ofc = "t1.fa"
os.system("bedtools getfasta -fi "+genome+" -bed "+inocn+" -fo "+ofc)

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

os.system("rm "+ofc)


