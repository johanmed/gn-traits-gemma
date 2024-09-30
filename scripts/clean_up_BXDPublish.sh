#!/usr/bin/env bash


csvcut -d, ImputedBXDPublish.csv | grep BXD | grep -v BXD_ | grep -wv BXD3 | grep -wv BXD223 | grep -wv BXD140 | grep -wv BXD96 | grep -wv BXD80 | grep -wv BXD103 | grep -wv BXD78/2 | grep -wv BXD147a | grep -wv BXDS34 | grep -wv BXD46 | grep -wv BXD47 | grep -wv BXD57 | grep -wv BXD58 | grep -wv BXD82 | grep -wv BXD065xBXD102F1 | grep -wv BXD077xBXD065F1 | grep -wv BXD0650BXD102F1 | grep -wv BXD0770BXD065F1 | grep -v "(BXD" | csvcut -d, -C 1 | less -S > cleaned_BXD_phenotypes.bimbam

