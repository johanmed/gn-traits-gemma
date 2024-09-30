#!/usr/bin/env python

import pandas as pd
import numpy as np
import os

gemma_files=[i for i in os.listdir() if 'assoc' in i and 'relevant' in i and 'new' not in i]
gemma_files=sorted(gemma_files)

info_read=open('BXD_traits_selected_info.csv').readlines()
info_read=sorted(info_read)

def add_desc_gemma_assoc(file, val):
        gemma_content=open(file).readlines()
        to_write=[]
        for u in gemma_content:
            to_write.append(f'{u.strip()}\t{val}')
            
        ready_to_write='\n'.join(to_write)
        gemma_write=open(f'new_{file}', 'w')
        gemma_write.write(ready_to_write)
            
def process_file(info_read, gemma_files, add_desc_gemma_assoc):
    for i, j in enumerate(info_read):
        x, y, z = j.split('\t')
        for f in gemma_files:
            o, p, q, r=f.split('_')
            l, m, n= r.split('.')
            if i==int(l[5:]) and y=='Diabetes trait':
                print(f'Inferred diabetes trait for {f}')
                add_desc_gemma_assoc(f, 0)
            elif i==int(l[5:]) and y=='Immune system trait':
                print(f'Inferred Immune system trait for {f}')
                add_desc_gemma_assoc(f, 1)
            elif i==int(l[5:]) and y=='Gut microbiome trait':
                print(f'Inferred Gut microbiome trait for {f}')
                add_desc_gemma_assoc(f, 2)

process_file(info_read, gemma_files, add_desc_gemma_assoc)
