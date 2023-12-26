def custom_sort(names):
    n = len(names)
    for i in range(n):
        for j in range(0, n-i-1):
            if names[j][0] > names[j+1][0]:
                names[j], names[j+1] = names[j+1], names[j]
            elif names[j][0] == names[j+1][0]:
                if len(names[j]) > 1 and len(names[j+1]) > 1 and names[j][1] > names[j+1][1]:
                    names[j], names[j+1] = names[j+1], names[j]
                elif names[j] > names[j+1]:
                    names[j], names[j+1] = names[j+1], names[j]
    
names = []
for _ in range(10):
    names.append(str(input()))
custom_sort(names)

print("Sorted names:", names)
