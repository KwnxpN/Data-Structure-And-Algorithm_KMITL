"""KKK"""

def convert(text_tup):
    """loads for tuple"""
    values = text_tup.strip('()').split(', ')
    return tuple(map(float, values))

def swapvar(data):
    """swap var x and y"""
    front, back = data[0], data[1]
    print((back, front))
swapvar(convert(input()))
