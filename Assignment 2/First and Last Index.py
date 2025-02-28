def first_last(arr,target):
    for i in range (len(arr)):
        if arr[i]== target:
            start=i
            while i+1 < len(arr) and arr[i+1]== target:
                i+=1
            return[start,i]
    return[-1,-1]
    
arr=[1,2,2,2,2,3,4]
target =2
print(first_last(arr,target))