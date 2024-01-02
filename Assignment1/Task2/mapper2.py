#!/usr/bin/env python3
import sys
#print(f"{product_id}\t{customer_id}\t{rating}\t{quantity}")

for line in sys.stdin:
    lines = line.strip().split('\t')
    if int(lines[2]) < 3:
        print(f"{lines[0]}\t{lines[1]}\t{lines[2]}\t{lines[3]}")

