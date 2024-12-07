#!/usr/bin/env bash

#gemma -g ../data/BXD_genotypes.bimbam -p ../data/cleaned_BXD_phenotypes.bimbam -a ../data/BXD_snps.txt -gk 1 -o ../output/BXD_relatedness

for i in {1..637}; do 
    output="BXD_Association_trait${i}"
    gemma -p ../data/cleaned_BXD_phenotypes.bimbam -n $i -g ../data/BXD_genotypes.bimbam -a BXD_snps.txt -k ../output/BXD_relatedness.cXX.txt -lmm 1 -o $output
done

