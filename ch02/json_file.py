import json
from pprint import pprint

json_path = "./testfile.json"
with open(json_path,'r') as opened_file:
    policy = json.load(opened_file)

policy['Statement']['Resource'] = 'S3'
pprint(policy)

with open(json_path,'w') as opened_file:
    policy = json.dump(policy, opened_file)
