# # Defining arr
# arr=[]
# arr=[20,30,40]
# print("Defined arr:",arr)

# # Accessing Value using Index
# print("Accessing 0th Element:",arr[0])

# # Transversing every element
# print("Elements in arr:")
# for i in arr:
#     print(i)

# # Appending (Add element at the last index)
# arr.append(10)
# print("Appending 10:",arr)

# # Inserting (At index we want)
# # Syntax arrName.insert(Index, Value)
# arr.insert(3,50) 
# print("Inserting:",arr)

# # Replace/Update
# arr[4]= 60
# print("Updating:",arr)

# # Pop (Delete last element in arr)
# arr.pop()
# print("Popping:",arr)

# # Removing (Using Value)
# arr.remove(20)
# print("Removing:",arr)

# # Return Size of arr
# print("Size of arr:",len(arr))

# # Finding element in arr
# arr=[10,20,100,13,30,101,40,50]
# key=30
# found=False
# for i in arr:
#     if i==key:
#         found=True
# print("Element Found:", found)

# # Finding largest element
# Largest=arr[0]
# for i in arr:
#     if i>Largest:
#         Largest=i
# print("Largest Element:",Largest)

# # Finding Smallest element
# Smallest=arr[0]
# for i in arr:
#     if i<Smallest:
#        Smallest=i
# print("Smallest element:",Smallest)

# # Sum of Elements in array
# total=0
# for i in arr:
#     total+=i
# print("Sum:",total)

# # Average of elements in array
# print("Average:", sum(arr)/len(arr))

# # Count Even and Odd elements in Array
# odd=0
# even=0
# for i in arr:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print("Count of Even elements:",even)
# print("Count of Odd elements:",odd)

# # Reversing a arr
# print("Reversing by slicing:", arr[::-1])

# # Reversing using Swapping
# start=0
# end=len(arr)-1

# start=0
# end=len(arr)-1

# while start<end:
#     arr[start],arr[end]= arr[end], arr[start]
#     start+=1
#     end-=1
# print("Reversing by Swapping", arr)

# # Slicing (Use to access specific part of arr)
# print("Slicing 1-4:", arr[1:5])
# print("Negative Slicing:", arr[5:1:-1])
# print("Slicing by other second element:",arr[::2])

# # Find the largest even number.
# Largest= None
# for i in arr:
#     if (i%2==0) and (Largest is None or i >Largest):
#         Largest=i
# print("Largest Even no.:",Largest)

# # Find the smallest odd number.
# minimum = None
# for i in arr:
#     if (i % 2 != 0) and (minimum is None or i < minimum):
#          minimum = i

# if minimum is None:
#     print("No odd number found")
# else:
#     print("Smallest Odd Number:", minimum)

# # Rotate an array left by one position.
# print(arr)
# temp=arr[0]
# for i in range(0,len(arr)-1):
#     arr[i]=arr[i+1]
# arr[len(arr)-1]=temp
# print(arr)

# # Rotate an array right by one position.
# print(arr)
# temp=arr[len(arr)-1]
# for i in range(len(arr)-1,0,-1):
#    arr[i]=arr[i-1]
# arr[0]=temp
# print(arr)

# # Move all zeros to the end.
# arr=[70,0,65,0,0,34]
# count=0
# arr2=[]
# for i in arr:
#     if i==0:
#         count+=1
#     else:
#         arr2.append(i)
# print(arr2+[0]*count)

# # Merge two arrays.
# arr=[1,2,3,4,5]
# arr2=[6,7,8,9]
# print(arr+arr2)

# # Find the difference between the largest and smallest element.
# Smallest=min(arr)
# Largest=max(arr)
# print(Largest-Smallest)

# # Check whether two arrays are identical.
# arr3=[1,2,3,4,5]
# found=False
# if arr==arr3:
#     found=True
# print(found)

# # Find the third largest element.

# # Count the frequency of every element.

# =======2D ARRAY =========

# EASY
# Q1. Create and Print
# Create a 3 × 3 matrix and print it.
array=[[1,2,3],[4,5,6],[7,8,9]]
print(array)

# Q2. Access an Element
# Print the element at:
# Row 2, Column 0
# Row 1, Column 1
array=[[1,2,3],[4,5,6],[7,8,9]]
print(array[2][0])
print(array[1][1])

# Q3. Traverse the Matrix
# Print every element one by one.
array=[[1,2,3],[4,5,6],[7,8,9]]
for i in array:
    for j in i:
        print(j)

# Q4. Print Row-wise
array=[[1,2,3],[4,5,6],[7,8,9]]
for i in range (0,len(array)):
    print(f"Row {i+1}: {array[i]}")

# Q5. Print Column-wise

#  Q6. Update an Element
# Replace 5 with 100.
array=[[1,2,3],[4,5,6],[7,8,9]]
array[1][1]=100
print(array)

# Q7. Count Total Elements
array=[[1,2,3],[4,5,6],[7,8,9]]
count=0
for i in array:
    for j in i:
        count+=1
print(count)

# Q8. Find Maximum Element
array=[[1,2,3],[64,5,16],[7,8,9]]
large=array[0][0]
for i in array:
    for j in i:
        if j>large:
            large=j
print(large)

# Q9. Find Minimum Element
array=[[1,2,3],[64,5,16],[7,8,9]]
small=array[0][0]
for i in array:
    for j in i:
        if j<small:
            small=j
print(small)

# Q10. Find Sum of All Elements
array=[[1,2,3],[64,5,16],[7,8,9]]
total=0
for i in array:
    for j in i:
        total+=j
print(total)