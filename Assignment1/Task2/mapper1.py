#!/usr/bin/env python3
import sys

#order, orderid, cutomerid,productid,quantity,priceperunit
#review, reviewid,productid,customerid,rating,reviewtext
for line in sys.stdin:
    fields=line.strip().split('\t')
    record_type=fields[0]
    if record_type=="order":
        order_id,customer_id,product_id,quantity,price=fields[1:]
        print(f"{product_id}\t{customer_id}\t{quantity}\tO")
    elif record_type=="review":
        review_id,product_id,customer_id,rating=fields[1:5]
        print(f"{product_id}\t{customer_id}\t{rating}\tR")
        
        
