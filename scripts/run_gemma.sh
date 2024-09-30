#!/usr/bin/env bash

#gemma -g BXD_genotypes.bimbam -p cleaned_BXD_phenotypes.bimbam -a BXD_snps.txt -gk 1 -o BXD_relatedness

for i in {1..637}; do 
    output="BXD_Association_trait${i}"
    gemma -p cleaned_BXD_phenotypes.bimbam -n $i -g BXD_genotypes.bimbam -a BXD_snps.txt -k output/BXD_relatedness.cXX.txt -lmm 1 -o $output
done

