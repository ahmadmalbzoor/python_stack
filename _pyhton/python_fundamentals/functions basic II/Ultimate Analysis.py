def print1(a):
    empty_dict={}
    min=0
    max=0
    avg=0
    sum=0
    for x in range(0,len(a),1):
        if a[x]<a[0]:
            min=a[x]
        if a[x]>a[0]:
            max=a[x]
        sum+=a[x]
    avg=sum/len(a)
    return {'sumTotal': sum, 'average': avg, 'minimum': min, 'maximum': max, 'length': len(a) }

print(print1(([1,2,1,-9])))

