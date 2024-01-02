#!/usr/bin/env python3
#print(f"{product_id}\t{quantity}")
import sys
cur_product=None
total_quan=0
for line in sys.stdin:
    fields=line.strip().split('\t')
    if cur_product is None:
        cur_product=fields[0]
    if cur_product!=fields[0]:
        #if cur_product:
        print(f"{cur_product}\t{total_quan}")
        cur_product=fields[0]
        total_quan=0
    total_quan+=int(fields[1])
if cur_product:
    print(f"{cur_product}\t{total_quan}")
    
