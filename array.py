# Defining arr
arr=[]
arr=[20,30,40]
print("Defined arr:",arr)

# Accessing Value using Index
print("Accessing 0th Element:",arr[0])

# Transversing every element
print("Elements in arr:")
for i in arr:
    print(i)

# Appending (Add element at the last index)
arr.append(10)
print("Appending 10:",arr)

# Inserting (At index we want)
# Syntax arrName.insert(Index, Value)
arr.insert(3,50) 
print("Inserting:",arr)

# Replace/Update
arr[4]= 60
print("Updating:",arr)

# Pop (Delete last element in arr)
arr.pop()
print("Popping:",arr)

# Removing (Using Value)
arr.remove(20)
print("Removing:",arr)

# Return Size of arr
print("Size of arr:",len(arr))

# Finding element in arr
arr=[10,20,100,13,30,101,40,50]
key=30
Found=False
for i in arr:
    if i==key:
        Found=True
print("Element Found:", Found)

# Finding largest element
max=arr[0]
for i in arr:
    if i>max:
        max=i
print("Largest Element:",max)

# Finding Smallest element
min=arr[0]
for i in arr:
    if i<min:
        min=i
print("Smallest element:",min)

# Sum of Elements in array
sum=0
for i in arr:
    sum+=i
print("Sum:",sum)

# Average of elements in array
print("Average:", sum/len(arr))

# Count Even and Odd elements in Array
odd=0
even=0
for i in arr:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Count of Even elements:",even)
print("Count of Odd elements:",odd)

# Reversing a arr
print("Reversing by slicing:", arr[::-1])

# Reversing using Swapping
start=0
end=len(arr)-1

while end<start:
    arr[start],arr[end]= arr[end]. arr[start]
    start+=1
    end-=1
print("Reversing by Swapping", arr)

# Slicing (Use to access specific part of arr)
print("Slicing 1-4:", arr[1:5])
print("Negative Slicing:", arr[5:1:-1])
print("Slicing by other second element:",arr[::2])

# Find the largest even number.
max= arr[0]
for i in arr:
    if (i%2==0) and (i>max):
        max=i
print("Largest Even no.:",max)

# Find the smallest odd number.
minimum = None
for i in arr:
    if (i % 2 != 0) and (minimum is None or i < minimum):
         minimum = i

if minimum is None:
    print("No odd number found")
else:
    print("Smallest Odd Number:", minimum)

# Rotate an array left by one position.

# Rotate an array right by one position.
# Move all zeros to the end.
# Count the frequency of every element.
# Merge two arrays.
# Find the difference between the largest and smallest element.
# Check whether two arrays are identical.
# Find the third largest element.