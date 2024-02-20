"""KKK"""
from json import loads
def is_intersect(list_a, list_b, list_c):
    """the function that check 3 lists intersection"""
    res = False
    list_a, list_b, list_c = loads(list_a), loads(list_b), loads(list_c)

    for num_a in list_a: #n
        for num_b in list_b:#n
            if num_b == num_a:
                for num_c in list_c: #n
                    if num_c == num_b:
                        res = True
    print(res)
is_intersect(str(input()), str(input()), str(input()))
