"""KKK"""

def liang(name):
    """liang ah"""
    nnn = len(name)
    for i in range(nnn):
        for j in range(0, nnn-i-1):
            if name[j][0] > name[j+1][0]:
                name[j], name[j+1] = name[j+1], name[j]
            elif name[j][0] == name[j+1][0]:
                if len(name[j]) > 1 and len(name[j+1]) > 1 and name[j][1] > name[j+1][1]:
                    name[j], name[j+1] = name[j+1], name[j]
                elif name[j] > name[j+1]:
                    name[j], name[j+1] = name[j+1], name[j]
    return name
def main(amount):
    """main here"""
    name_lists = []
    for _ in range(amount):
        name_lists.append(str(input()))
    res = liang(name_lists)
    print(*res, sep="\n")
main(int(input()))
