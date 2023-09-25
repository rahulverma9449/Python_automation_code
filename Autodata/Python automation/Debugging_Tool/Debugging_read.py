

import json
import pdb

with open('./create_order-payload.json', 'r') as f:
    content = json.load(f)

print(content)
pdb.set_trace()

print("Done !!")

