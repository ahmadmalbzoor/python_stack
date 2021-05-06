def print1(a):
    min=a[0]
    for x in range(0,len(a),1):
        if a[x]<min:
            min=a[x]
    return min
print(print1([4,1,2,5]))