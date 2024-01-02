#!/usr/bin/env python3
#print(f"{product_id}\t{customer_id}\t{rating}\t{quantity}")
import sys

for line in sys.stdin:
    fields=line.strip().split('\t')
    product_id,customer_id,rating,quantity=fields
    print(f"{product_id}\t{customer_id}\t{rating}\t{quantity}")
