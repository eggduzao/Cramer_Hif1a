#!/bin/zsh

# Fastq-dump

fastq-dump.2.4.5 --split-files SRR1653776.sra
fastq-dump.2.4.5 --split-files SRR1653777.sra

# Trimming

trim_galore --no_report_file --suppress_warn -o ./ SRR1653776_1.fastq &> /dev/null
trim_galore --no_report_file --suppress_warn -o ./ SRR1653777_1.fastq &> /dev/null

# Read Mapping

bowtie2 -x mm9 -U SRR1653776_1_trimmed.fq -S SRR1653776.sam -X 2000 --no-mixed --no-discordant
bowtie2 -x mm9 -U SRR1653777_1_trimmed.fq -S SRR1653777.sam -X 2000 --no-mixed --no-discordant

##### SRR1653776:
#7617278 reads; of these:
#  7617278 (100.00%) were unpaired; of these:
#    677385 (8.89%) aligned 0 times
#    4886984 (64.16%) aligned exactly 1 time
#    2052909 (26.95%) aligned >1 times
#91.11% overall alignment rate
##### SRR1653777:
#6004111 reads; of these:
#  6004111 (100.00%) were unpaired; of these:
#    283581 (4.72%) aligned 0 times
#    4182349 (69.66%) aligned exactly 1 time
#    1538181 (25.62%) aligned >1 times
#95.28% overall alignment rate

# Create BAM

samtools view -Sb SRR1653776.sam > SRR1653776.bam
samtools sort SRR1653776.bam SRR1653776_sorted
samtools index SRR1653776_sorted.bam
samtools rmdup -sS SRR1653776_sorted.bam SRR1653776_remdup.bam
samtools view -bq 30 SRR1653776_remdup.bam > SRR1653776.bam
samtools index SRR1653776.bam
rm SRR1653776.sam SRR1653776.sra SRR1653776_1.fastq SRR1653776_1_trimmed.fq  SRR1653776_sorted.bam SRR1653776_remdup.bam SRR1653776_sorted.bam.bai

samtools view -Sb SRR1653777.sam > SRR1653777.bam
samtools sort SRR1653777.bam SRR1653777_sorted
samtools index SRR1653777_sorted.bam
samtools rmdup -sS SRR1653777_sorted.bam SRR1653777_remdup.bam
samtools view -bq 30 SRR1653777_remdup.bam > SRR1653777.bam
samtools index SRR1653777.bam
rm SRR1653777.sam SRR1653777.sra SRR1653777_1.fastq SRR1653777_1_trimmed.fq  SRR1653777_sorted.bam SRR1653777_remdup.bam SRR1653777_sorted.bam.bai

# Merge BAM and quality

samtools merge ATAC_merged.bam SRR1653776.bam SRR1653777.bam
samtools sort ATAC_merged.bam ATAC
samtools index ATAC.bam
rm ATAC_merged.bam

samtools flagstat ATAC.bam > atac_stats.txt

# Call Peaks

macs2 callpeak -t ATAC.bam -n LI_ATAC -f BAM -g mm --nomodel --nolambda --keep-dup auto

# Fix Peaks
grep -v -E 'chrY|chrM|random|chrUn' LI_ATAC_peaks.bed > temp.bed
bedtools slop -i temp.bed -g /hpcwork/izkf/projects/TfbsPrediction/Data/MM9/mm9.chrom.sizes -b 20 > LI_ATAC_peaks_format.bed
cut -f 1,2,3 LI_ATAC_peaks_format.bed > LI_ATAC_peaks_format_cut.bed
rm temp.bed


