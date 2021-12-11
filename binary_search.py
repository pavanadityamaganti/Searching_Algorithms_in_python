n=int(input())          #to take the length of the array from the user
arr=[]
for i in range(n):
    x=int(input())      # to take all the elements to the array of given length 
    arr.append(x)
arr.sort()
k=int(input())          #to take the key value to be found in the array
l=0
u=len(arr)
while l<=u:
    mid=l+u//2
    if mid<len(arr):
        if arr[mid]==k:
            print("The value is present in list")
            break
        else:
            if arr[mid]>k:
                u=mid
            else:
                l=mid
    else:
        print("The key value is not present in given list")
        break
else:
    print("The key value is not present in given list")
