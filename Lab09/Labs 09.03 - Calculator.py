"""KKK"""

def calculator(num):
    """count how many times we press the calculator button"""
    res = 0
    if num == 1:
        print(1)
    else:
        for amount in range(1, num+1):
            res += len(str(amount))
        print(res + num)
calculator(int(input()))
