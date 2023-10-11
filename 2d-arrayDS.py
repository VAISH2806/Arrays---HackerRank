ans = [] 
def values(start,center,end):
    
    for i in range(4):
        sums = 0
        zero=i 
        first=i+3
        for a in range(zero,first):
            sums+=arr[start][a]
        for k in range(zero+1,zero+2):
            sums+=arr[center][k]
        for e in range(zero,first):
            sums+=arr[end][e]
        ans.append(sums)
        
def hourglassSum(arr):
    # Write your code here
    start = 0
    while start <= 3:
        center=start+1 
        end=center+1 
        values(start,center,end)
        start+=1
    return max(ans)
