#!/usr/bin/env python3
# {product_id}\t{customer_id}\t{quantity}\t{O}

#import sys

#lines=[line.strip().split('\t') for line in sys.stdin]
##num_lines=len(lines)

#for i in range(num_lines):
#    fields1=lines[i]
 #   for j in range(i+1,num_lines):
#        fields2=lines[j]
 #       if fields1[1]==fields2[1] :
 #           fields1.append(fields2[2])
#           if "R" in fields1:
 #               quantity=fields1[4]
 #               rating=fields1[2]
 #               customer_id,product_id,rating,record_type,quantity=fields1
 #               print(f"{product_id}\t{customer_id}\t{rating}\t{quantity}\tR")
  #          else:
   #             quantity=fields1[2]
   #           rating=fields1[4]
   #             customer_id,product_id,quantity,record_type,rating=fields1
   #             print(f"{product_id}\t{customer_id}\t{rating}\t{quantity}\tO")
               
               
               
import sys
cur_product_id=None
cur_customer_id=None
cur_quan=0
cur_rating=0
#record_dict = {}

for line in sys.stdin:
    fields = line.strip().split('\t')
    product_id = fields[0]
    customer_id = fields[1]
    record_type = fields[3]
    if(product_id==cur_product_id and customer_id==cur_customer_id and record_type!=cur_record_type):
        if record_type=="R":
           #print("1")
           cur_rating=fields[2]
           customer_id,product_id,rating,record_type=fields
    	        #print(f"{product_id}\t{customer_id}\t{rating}\t{quantity}\tR")
        else:
    	   # print("2")
    	    cur_quan=fields[2]
    	    customer_id,product_id,quantity,record_type=fields
    	    #print(f"{product_id}\t{customer_id}\t{rating}\t{quantity}\tO")
        temp1=cur_rating
        temp2=cur_quan
        print(temp1,temp2)
        print(f"{product_id}\t{customer_id}\t{cur_rating}\t{cur_quan}")
    else:
        cur_product_id=product_id
        cur_customer_id=customer_id
        cur_record_type=record_type
    
    


