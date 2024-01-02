#!/usr/bin/env python3

import sys
import json

for line in sys.stdin:
    try:
        records=line.strip().strip('[').strip(']').strip(',')
        record=json.loads(records)
        batsman_name=record.get("name","")
        runs=int(record.get("runs",0))
        balls_faced=int(record.get("balls",0))
        
        if balls_faced>0:
            strike_rate=(runs/balls_faced)*100
        else:
            strike_rate=0.0
        strike_rate=round(strike_rate,3)
        print(f"{batsman_name}\t{strike_rate}")
    except Exception as e:
        continue


        
        
        
        
        
        
        
        
        
        
        
                                                                                    
        
