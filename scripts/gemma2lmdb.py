#!/usr/bin/env python3
#
# Note that the chr+position is used in the key where position is
# stored big-endian to allow for proper sorting(!) X and Y chromosomes
# are stored as their ASCII value (88 and 89(.
#
# The records contain the standard gemma output stored as floats.
#
# The conversion will fail if:
#
# - two markers share the same position

import sys
import argparse
import json
import lmdb
from struct import *

parser = argparse.ArgumentParser(description='Turn GEMMA assoc output into an lmdb db.')
parser.add_argument('--db',default="project.mdb",help="DB name")
parser.add_argument('--meta',required=False,help="JSON meta file name")
parser.add_argument('files',nargs='*',help="GEMMA file(s)")
args = parser.parse_args()

# ASCII
X=ord('X')
Y=ord('Y')

meta = { "type": "gemma-assoc",
         "version": 1.0,
         "key-format": ">cL",
         "rec-format": "=ffff" }
log = {} # track output log
hits = [] # track hits

with lmdb.open(args.db,subdir=False) as env:
    for fn in args.files:
        print(f"Processing {fn}...")
        if "log" in fn:
            with open(fn) as f:
                log[fn] = f.read()
        else:
            with open(fn) as f:
                with env.begin(write=True) as txn:
                    for line in f.readlines():
                        cont=line.rstrip('\n').split('\t')
                        chr,rs,pos,miss,a1,a0,af,beta,se,l_mle,p_lrt, desc = line.rstrip('\n').split('\t')
                        if chr=='chr':
                            continue
                        if (chr =='X'):
                            chr = X
                        elif (chr =='Y'):
                            chr = Y
                        else:
                            chr = abs(int(chr))
                        # print(f"chr={chr}, type={type(chr)}")
                        chr_c = pack('c',bytes([chr]))
                        # print(chr,chr_c,rs)
                        # key = (chr+'_'+pos).encode()
                        key = pack('>cL',chr_c,abs(int(pos)))
                        test_chr_c,test_pos = unpack('>cL',key)
                        assert chr_c == test_chr_c
                        assert test_pos == abs(int(pos))
                        test_chr = unpack('c',chr_c)
                        # assert test_chr == int(chr), f"{test_chr} vs {int(chr)} - {chr}"
                        val = pack('=ffffff', float(af), float(beta), float(se), float(l_mle), float(p_lrt), float(desc))
                        res = txn.put(key, bytes(val), dupdata=False, overwrite=False)
                        if res == 0:
                            if float(p_lrt) > 2.0:
                                hits.append([chr,int(pos),rs,p_lrt])
                        else:
                             print(f"WARNING: failed to update lmdb record with key {key} -- probably a duplicate {chr}:{pos} ({test_chr_c}:{test_pos})")
    with env.begin() as txn:
        with txn.cursor() as curs:
            # quick check and output of keys
            for (key, value) in list(txn.cursor().iternext()):
                if key==b'meta':
                    continue
                else:
                    chr,pos = unpack('>cL',key)
                    chr_c=int.from_bytes(chr)
                    print(chr_c,pos)
                    af, beta, se, l_mle, p_lrt, desc= unpack('=ffffff', value)
                    print(af, beta, se, l_mle, p_lrt, desc)

    meta["hits"] = hits
    meta["log"] = log
    print("HELLO: ",file=sys.stderr)
    print(meta,file=sys.stderr)
    with env.begin(write=True) as txn:
        res = txn.put('meta'.encode(), json.dumps(meta).encode(), dupdata=False, overwrite=False)
