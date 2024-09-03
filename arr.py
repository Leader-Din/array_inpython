#<============================================>

# import array as arr
# a = arr.array('i', [1, 2, 3])
# print("The new created array is : ", end=" ")
# for i in range(0, 3):
#     print(a[i], end=" ")
# print()
# b = arr.array('d', [2.5, 3.2, 3.3])
# print("\nThe new created array is : ", end=" ")
# for i in range(0, 3):
#     print(b[i], end=" ")

#<================================================>

# arr = [1, 2, 3, 4]
# for index in range(len(arr)):
#     value = arr[index]
#     print("hello", str(index))

#mre customizable#

#<=================================================>

# arr = [1, 2, 3, 4]
# for value in arr:
#     print("hello", str(value))

#short way to loop#

#<================================================>

# list1 = [5, 4, 7, 3, 1]
# list2 = list1
# list1[0] = 99

# print(list1[0])
# print(list2[0])

#<===================================================>

# a = 5
# b = a
# a = 7
# print(b)

#<===================================================>

# def countNegNum(arrOfNum):
#     numNeg = 0
#     for num in arrOfNum:
#         if num < 0:
#             numNeg += 1
#     if num == 0:
#         return -1
#     return numNeg

# numbers = eval(input("Enter the arr: "))

# print(countNegNum(numbers))

#<===================================================>

# def getIndexMinNumber(arr):
#     min_index = 0
#     for i in range(len(arr)):
#         if arr[i] < arr[min_index]:
#             min_index = i

#     return min_index

# numbers = eval(input("Enter the arr: "))

# print(getIndexMinNumber(numbers))

#<===================================================>

# def getIndexOfNumberFive(anarray):
#     i = 0
#     isFoundFive = False
#     resoult = None
#     while i <len(anarray) and not isFoundFive:
#         if anarray[i] == 5:
#             isFoundFive = True
#             resoult = i
#         i += 1
#     return resoult

# number = eval(input("Enter the array: "))
# print(getIndexOfNumberFive(number))

#////////////////////////////////////////////////////////////////

# def getIndexOfNumberFive(anarray):
#     result = 0
#     for i in range(len(anarray)):
#         if anarray[i] == 5:
#             result = i
    
#     return result

# number = eval(input("Enter the array: "))
# print(getIndexOfNumberFive(number))

#<===================================================>

# def sumOddEvenNumber(arr):
#     sumOdd = 0
#     sumEven = 0
#     for i in range(len(arr)):
#         if arr[i] % 2 == 1:
#             sumOdd += arr[i]
#         if arr[i] % 2 == 0:
#             sumEven += arr[i]
#     return "odd", sumOdd, "even", sumEven

# numbers = eval(input("Enter the array: "))
# print(sumOddEvenNumber(numbers))

#<===================================================>

# def replaceNumber(arr):
#     for i in range(len(arr)):
#         if arr[i] == 9:
#             arr[i] = 168
#     return arr
# numbers = eval(input("Enter array: "))
# print(replaceNumber(numbers))

#<===================================================>

# def replace_letter(arr):
#     result = []
#     for i in arr:
#         new_string = ""
#         for j in i:
#             if j == "a" or j == "A":
#                 new_string += "$"
#             else:
#                 new_string += j
#         result.append(new_string)
#     return result
# name = eval(input())
# print(replace_letter(name))

#<===================================================>

# def sum_of_arrays(array1, array2):
#     sum1 = sum(array1)
#     sum2 = sum(array2)
#     return sum1, sum2

# array1 = eval(input("Enter array1: "))
# array2 = eval(input("Enter array2: "))

# print(sum_of_arrays(array1, array2))

#<===================================================>

# a = [1, 3, 4]
# b = [a[0], a[1], a[2]]
# a[0] = 7
# print(b[0])

#<===================================================>

# arr = [1, 2, 3, 4, 5]
# arr.append(6)
# print(arr)
#<===================================================>
# arr = [1, 2, 3, 4, 5]
# color = ["white", "balck", "pink"]
# arr.extend(color)
# print(arr)

#<===================================================>

text = "RONAN"
arr_Text = []
for i in range(len(text)):
    arr_Text.append(text[i])
print(arr_Text)