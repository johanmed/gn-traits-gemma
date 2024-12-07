#!/usr/bin/env bash

cd ../output/

for i in BXD_Association_trait*.assoc.txt; do output="relevant_${i}"; csvcut -t -C 10 $i | sed 's/,/\t/g' > ${output}; done

for i in BXD_Association_*.log.txt; do output="relevant_${i}"; cp $i ${output}; done
