def binarysearch(a,first,last,key):
        while first<=last:
                mid=(first+last)//2
                if a[mid]==key:
                        return mid
                elif(a[mid]<key):
                        first=mid+1
                else:
                        last=mid-1
        return -1
a=[]
n=int(input("Enter number of elements:"))
for i in range(0,n):
        a.append(int(input()))
key = int(input("enter key:"))
pos = binarysearch(a, 0, n-1, key)
if (pos == -1):
        print("Element not found")
else:
        print("Element found at index:", pos+1)
