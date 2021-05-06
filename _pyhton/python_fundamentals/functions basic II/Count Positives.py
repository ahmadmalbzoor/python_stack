def print1(a):
    sum=0
    for x in range(0,len(a),1):
        if a[x]>0:
            sum+=a[x]
            
    return sum
print(print1([-1,4,1,1]))
