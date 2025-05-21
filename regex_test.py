import re
import regex

# password validering
# tal, store bogstaver, små bogstaver og udvidet specialtegn, midst 16 karakterer
def password_test1():
    assert regex.validate_password("123abc123abc123abc123abc") == False

def password_test2():
    assert regex.validate_password("123abc123abc123abc123abc_ABC||") == True

def password_test3():
    assert regex.validate_password("123123123123123123123123123123123123") == False
# Ipv4 validering

# email adresse validering