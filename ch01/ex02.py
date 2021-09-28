# Write a Python function that takes a string as an argument and prints whether it is upper- or lowercase.

def check_case(string_to_test):
    if string_to_test.islower():
        print("lower")
    elif string_to_test.isupper():
        print("upper")
    else:
        print("nothing special")

str01 = "TEST"
str02 = "test"
str03 = "tEsT"

check_case(str01)
check_case(str02)
check_case(str03)
