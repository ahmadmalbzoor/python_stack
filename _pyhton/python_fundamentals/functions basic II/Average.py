def print1(a):
    sum=0
    avg=0
    for x in range(0,len(a),1):
        sum+=a[x]
    avg=sum/len(a)
    return avg
print(print1([1,2,3,4]))