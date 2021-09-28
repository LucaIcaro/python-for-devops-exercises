import yaml
from pprint import pprint

with open('testfile.yml','r') as open_file:
    verify_yaml = yaml.safe_load(open_file)

pprint(verify_yaml)