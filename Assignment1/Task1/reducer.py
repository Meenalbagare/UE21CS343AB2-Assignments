#!/usr/bin/env python3

import sys
import json
from collections import defaultdict

batsman_stats=defaultdict(list)
for line in sys.stdin:
    try:
        parts=line.strip().split('\t')
        batsman_name=parts[0]
        strike_rate=float(parts[1])
        batsman_stats[batsman_name].append(strike_rate)
    except Exception as e:
        continue
for batsman,strike_rates in batsman_stats.items():
    avg_strike_rate=sum(strike_rates)/len(strike_rates)
    avg_strike_rate=round(avg_strike_rate,3)
    output={"name": batsman, "strike_rate": avg_strike_rate}
    output_json=json.dumps(output)
    print(output_json)
