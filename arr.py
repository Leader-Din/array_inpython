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

# text = "RONAN"
# arr_Text = []
# for i in range(len(text)):
#     arr_Text.append(text[i])
# print(arr_Text)

#<===================================================>

# number = 1, 2, 4, 5
# my_num = []

# for i in range(len(number)):
#     my_num.append(number[i])

# print(my_num)

#<===================================================>

# numbers = [10, 20, 30, 40]
# numbers.insert(0, 100)
# print(numbers)

#<===================================================>

# numbers = [10, 20, 30, 40]
# numbers.pop(3)
# print(numbers)

#<===================================================>


#excercice1
# frouites = []
# frouites.append("apple")
# frouites.append("banana")
# frouites.append("cherry")
# print(frouites)

#ex 2

# •	Task: Write a loop that asks the user to input 5 of their favorite foods and appends each one to a list called favorite_foods. Print the final list.

# favorite_foods = []
# for i in range(5):
#     favoriteFood = input("Enter your favorite food: ")
#     favorite_foods.append(favoriteFood)

# print(favorite_foods)

# ex 3
# •	Task: Start with the list colors = ["red", "blue", "green"]. Insert the color "yellow" at index 1. Print the updated list.

# colors = ["red", "blue", "green"]
# colors.insert(1, "yellow")
# print(colors)

#ex 4
#•	Task: Given the list numbers = [10, 20, 30, 40], insert the number 25 at index 2 and append the number 50 to the end of the list. Print the final list.

# numbers = [10, 20, 30, 40]
# numbers.insert(2, 25)
# numbers.append(50)
# print(numbers)

#ex5
# •	Task: Create a list animals = ["dog", "cat", "bird", "fish"]. Use the pop method to remove the last item from the list. Print the updated list and the removed item.
# animals = ["dog", "cat", "bird", "fish"]
# animals.pop(3)
# print(animals)

#ex 6
#•	Task: Given the list cities = ["New York", "Los Angeles", "Chicago", "Houston"], use the pop method to remove the city at index 1. Print the updated list and the removed city.
# cities = ["New York", "Los Angeles", "Chicago", "Houston"]
# cities.pop(1)
# print(cities)

#ex7
#•	Task: Start with an empty list called shopping_list. Append "milk" and "bread" to the list. Insert "eggs" at the beginning of the list. Then, use pop to remove the last item from the list. Print the final list.

# shopping_list = []
# shopping_list.append("milk")
# shopping_list.append("bread")
# shopping_list.insert(0, "eggs")
# shopping_list.pop(2)
# print(shopping_list)

# ex 8

#•	Task: Create a list called tasks = ["homework", "clean room", "exercise"]. Insert "read book" at index 1, append "cook dinner" to the end, and then remove the first item using pop(0). Print the final list

# tasks = ["homework", "clean room", "excercice"]

# tasks.insert(1, "read book")
# tasks.append("cook dinner")
# tasks.pop(0)

# print(tasks)

#ex 9
#•	Task: Write a function append_multiple(array, items) that takes an array array and another array items. Append each item from items to array and return the updated array.

# def append_multiple(array, items):
#     for item in items:
#         array.append(item)
    
#     return array
# array = eval(input("Enter your array: "))
# items = eval(input("Enter your items: "))
# print(append_multiple(array, items))

	
# arrayToSum = [1, 3, 9, 10, 20]
# total = 0
# i = 0
# while i < len(arrayToSum) :
#     total += int(arrayToSum[i])
#     i += 1
# print(total)

# array = [-5, 2, 9, -10, 0]
# i = 0
# while i < len(array) :
#     print(array[i])
# i+=1

# numbers = [55, 4, 92, 1, 104, 64, 73, 99, 20]
# max_value = numbers[0]

# for num in numbers :
#     if num > max_value :
#         max_value = num

# print('Maximum value:', max_value)

# team 1

# def findNumberBetweenEightandTwelve(arr):
    
#     if not arr:
#         return True
#     for i in range(len(arr)):
#         if 8 < arr[i] < 12:
#             return True
#     return False
# arr = eval(input("Enter a list of numbers: "))
# print(findNumberBetweenEightandTwelve(arr))

#team 2


# def extract_between_1_and_0(lst):
#     result = []
#     found_one = False
#     for num in lst:
#         if num == 1:
#             found_one = True
#             result = []
#         elif num == 0 and found_one:
#             return result
#         elif found_one:
#             result.append(num)
#     return []

# lst = eval(input("Enter a list: "))
# print(extract_between_1_and_0(lst))

#team 3
# Check if average of array is greater than 50 print “Pass” otherwise print “Fail”.

# def fineNum(array):
#     index = 0
#     result = 0
#     result1 = ""
#     for i in range(len(array)):
#         result += array[i]
#         index += 1
#     if result / index > 50:
#         result1 = "Pass"
#     else:
#         result1 = "fail"
#     return result1
# num = eval(input())
# print(fineNum(num))

# def check_average(arr):
#     if len(arr) == 0:
#         print("Fail")
#     else:
#         avg = sum(arr) / len(arr)
#         if avg > 50:
#             print("Pass")
#         else:
#             print("Fail")
# arr = eval(input("Enter an arr: "))
# check_average(arr)

# ex 4
#•	Check how many True Boolean value in array

# def check_bool(arr):
#     count = 0
#     for i in range(len(arr)):
#         if arr[i] == True:
#             count += 1
    
#     return count

# arr = eval(input("Enter an arr: "))
# print(check_bool(arr))

#ex 5
#•	Input a number
#	Display even numbers from 0 till that number

# def display_even_numbers(n):
#     num = 0
#     result = ""
    
#     while num <= n:
#         result += str(num) + " "
#         num += 2
#     return result

# number = int(input("Input a number: "))
# print(display_even_numbers(number))
