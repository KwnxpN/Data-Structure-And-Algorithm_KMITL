"""KKK"""

def is_even(num):
    """Is Even no %"""
    #return True if int((num//2)*2) == num else False
    return True if num[-1] in "02468" else False
print(is_even(str(input())))
