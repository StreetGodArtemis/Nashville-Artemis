#!/usr/bin/env python3
import re

with open('research_buffer.xml', 'r') as f:
    content = f.read().lower()
    
methods = re.findall(r'\b(wormhole|tipler|alcubierre|kerr|godel|cosmic|zeno|novikov|deutsch|loschmidt|tachyonic|visser|horowitz|hartle|everett|sorkin)\b', content)
print(f"TIME TRAVEL METHODS: {len(methods)} found")

feas = {'iter':10, 'butterfly':0.9955, 'cold_fusion':0.002, 'decoherence':1e-6, 'time_travel':1e-40}
print("
RANKED BY Q:")
for k,v in sorted(feas.items(), key=lambda x:x[1], reverse=True):
    print(f"{k}: Q={v:.2e}")

print("
UNIVERSAL PATH: ITER (Q=10)")
print("FIRST STEP: Garage fusor + 222.4Hz validation")
