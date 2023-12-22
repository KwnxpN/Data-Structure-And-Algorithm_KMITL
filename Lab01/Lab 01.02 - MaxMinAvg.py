"""KKK"""
from json import loads
def khunsangon(info_list):
    """max min avg"""
    most_num = less_num = info_list[0]
    for num in info_list:
        if num > most_num:
            most_num = num
        if num < less_num:
            less_num = num
    avg = round(sum(info_list) / len(info_list), 2)
    if ".0" in str(avg):
        avg = int(avg)
    print((most_num, less_num, avg))
khunsangon(loads(str(input())))
