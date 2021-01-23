def insertionsort(b):
    for i in range(1,len(b)):
        up=b[i]
        j=i-1
        while j>=0 and b[j]>up:
            b[j +1] = b[j]
            j-= 1
        b[j + 1]= up
    return b

def bucketsort(x):
    arr = []
    slot=10
    for i in range(slot):
        arr.append([])
    for j in x:
        index = int(slot * j)
        arr[index].append(j)
    for i in range(slot):
        arr[i]=insertionsort(arr[i])
    k=0
    for i in range(slot):
        for j in range(len(arr[i])):
            x[k]=arr[i][j]
            k += 1
    return x
x=[0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print("Sorted Array is ")
print(bucketsort(x))
                
