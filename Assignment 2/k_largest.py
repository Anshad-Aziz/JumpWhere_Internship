def k_largest(arr,k):
    n=len(arr)
    arr.sort()
    return arr[n-k]
    
arr=[6,5,4,3,2,1]
k=2
print(k_largest(arr,k))