import json
from pprint import pprint

file_path = "./testfile.txt"
open_file = open (file_path,'r')

# text_from_file = open_file.read()
# print (text_from_file)
# print(text_from_file[2])

# text_from_file = open_file.readlines()
# print(text_from_file[2])

open_file.close()

with open (file_path,'r') as open_file:
    text = open_file.readlines()

print(text)
