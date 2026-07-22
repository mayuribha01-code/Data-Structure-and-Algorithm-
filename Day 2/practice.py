# Count positive, negative, and zero elements.
# arr=[10,56,-26,100,-15,85]
# pos=0
# neg=0
# zer=0
# for i in arr:
#     if (i>0):
#         pos+=1
#     elif(i<0):
#         neg+=1
#     else:
#         zer+=1
# print("Positive:",pos)
# print("Negative:",neg)
# print("Zero:",zer)

# # Reverse the array (modify the original array).
# start=0
# end=len(arr)-1

# while start< end:
#     arr[start], arr[end]= arr[end], arr[start]
#     start+=1
#     end-=1
# print(arr)

# Find the largest element.
# large=arr[0]
# for i in arr:
#     if i> large:
#         large=i
# print(arr)
# print(large)

# # Find the second largest element.

# large=arr[0]
# sec=arr[0]
# third=arr[0]
# for i in arr:
#     if i>large:
#         sec=large
#         large=i
#     elif large>i>sec:
#         sec=i

# print(large)
# print(sec)

# # Find the second smallest element.

# min=arr[0]
# sec=arr[0]
# for i in arr:
#     if i<min:
#         sec=min
#         min=i
#     elif min<i<sec:
#         sec=i
# print(min)
# print(sec)

# # Check whether an element exists in the array.
# print(arr)
# key=int(input('Enter a ele:'))

# for i in range (len(arr)):
#     if arr[i]==key:
#         print("Key found at:",i)
# 
# # Check whether an element exists in the array
# arr=[10,556,10,65,34,10]
# num=int(input("Enter ele:"))
# count=0
# for i in arr:
#     if(i==num):
#         count+=1
# print(count)    

#Remove all occurrences of a number.
# arr=[10,10,14,10,10,20]
# num=int(input("Enter element to remove:"))
# while num in arr:
#         arr.remove(num)
# print(arr)

# # Copy one array into another.
# arr=[10,30,54,96]
# copy=[]
# for i in arr:
#     copy.append(i)
# print(copy)

# # Merge two arrays.
# print(arr+copy)

# # Find the difference between the largest and smallest element.
# min=arr[0]
# max=arr[0]
# for i in arr:
#     if i<min:
#         min=i
#     if i>max:
#         max=i
# print("Difference:",max-min)

# # Find the total of only odd numbers.
# sum=0
# for i in arr:
#     if (i%2!=0):
#         sum+=i
# print(sum)

# # Find the total of only even numbers.
# sum=0
# for i in arr:
#     if (i%2==0):
#         sum+=i
# print(sum)

# Check if the array is sorted in ascending order.

# Palidrone
x=122
def is_palindrome(x):
    x = str(x)
    return x == x[::-1]
print(is_palindrome(x))

