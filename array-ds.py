def reverseArray(a):
    # Write your code here
    length = len(a)-1
    count = 0
    while length!=count and length!=count-1:
        temp = a[count]
        a[count]=a[length]
        a[length]= temp
        count +=1
        length -=1
    return a
