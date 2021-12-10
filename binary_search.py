l=[]
m=int(input())  #takes's the length of array 
for i in range(m):
    x=int(input())#take's all the elements in array of given length
    l.append(x)
c=0
ans=0
n=int(input())#take's the key value that is used to find in array 
for i in range(len(l)):
    if l[i]==n:
        ans=i
        c+=1
        break
if c==1:
    print("the element",n,"is found at index",ans,"of array")
else:
    print("the element",n,"is not found")
