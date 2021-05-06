def print1(a):
    max=a[0]
    for x in range(0,len(a),1):
        if a[x]>max:
            max=a[x]
    return max
print(print1([4,1,2,5]))