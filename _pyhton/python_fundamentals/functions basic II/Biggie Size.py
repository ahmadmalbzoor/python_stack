def print1(a):
    for x in range(0,len(a),1):
        if a[x]>0:
            a[x]="big"
    print(a)
print((print1([1,-4,3,-3])))