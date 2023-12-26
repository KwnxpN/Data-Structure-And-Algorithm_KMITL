"""KKK"""

def bangna_trad(kilometers):
    """check kilo"""
    if 0 <= kilometers <= 5.032:
        print("Bangkok")
    elif 5.032 <= kilometers <= 35.477:
        print("Samut Prakarn")
    elif 35.477 <= kilometers <= 52.900:
        print("Chachoengsao")
    elif 52.900 <= kilometers <= 58.855:
        print("Chon Buri")
    else:
        print("InValid")
bangna_trad(float(input()))
