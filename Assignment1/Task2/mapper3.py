#!/usr/bin/env python3
#print(f"{product_id}\t{customer_id}\t{rating}\t{quantity}")
import sys

for line in sys.stdin:
    line = line.strip().split('\t')
    product_id,customer_id,rating,quantity=line
    print(f"{customer_id}\t{quantity}")
