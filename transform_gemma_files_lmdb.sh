#!/usr/bin/env bash

for i in ./BXD_GWA_trait*.assoc.txt; do output="test_${i}"; csvcut -t -C 10 $i | sed 's/,/\t/g' > ${output}; done

for i in ./BXD_GWA_*.log.txt; do output="test_${i}"; cp $i ${output}; done
