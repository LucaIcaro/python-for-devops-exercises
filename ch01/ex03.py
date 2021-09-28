# Write a list comprehension that results in a list of every letter in the word smog-tether capitalized.

str_to_parse = "smog-tether"
print ([x.upper() for x in str_to_parse if x.isalnum()])