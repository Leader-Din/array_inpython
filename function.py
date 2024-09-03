#<================================================================>
# def hi():
#     return 'hi'
# print(hi())

#<================================================================>
# def name(last_name, first_name):
#     return f"{last_name} {first_name}"
# print(name("Din", "Leader"))

#<================================================================>
# def hello():
#     return "Hello"
# print(hello())

#<================================================================>

# def hello_yon():
#     return "hello yon"
# print(hello_yon())

#<================================================================>

# def hello_sophy():
#     return "hello sophy"
# print(hello_sophy())

#<================================================================>

# def hello_sinh():
#     return "hello sinh"
# print(hello_sinh())

#<================================================================>

# def hello(name):
#     return "hello " + name

# print(hello("yon"))
# print(hello("sopy"))
# print(hello("sinh"))

#<================================================================>
# def hello(name, age):
#     return "Hello " + name + " Your age is: " + str(age)
# print(hello("Yon", 20))
# print(hello("Sophu", 18))
# print(hello("sinh", 17))
#<================================================================>
# def sum_number(a, b):
#     return a + b 
# print(sum_number(10, 20))
# print(sum_number(40, 50))
# print(sum_number(70, 10))

#<================================================================>

# def countp_letter_a(str):
#     countp_letter_a = 0
#     for i in range(len(str)):
#         if str[i] == 'a':
#             countp_letter_a += 1
#     return countp_letter_a
# print(countp_letter_a("avcda"))

#<=================================================================>
# ex 1
# def sum(num):
#     sum = 0
#     for i in range(len(num)):
#         sum += int(num[i])
#     return sum
# print(sum("123456"))
#<=================================================================>
#ex2

# def find_number(odd):
#     sum = 0
#     for i in range(len(odd)):
#         if int(odd[i])  % 2 == 1:
#             sum += int(odd[i])
#     return sum
        
# print(find_number("123456"))
#<=================================================================>
#ex3
# find min number
# def find_min(minnumber):
#     min = 0
#     min = minnumber[0]
#     for i in range(len(minnumber)):
#         if int(minnumber[i]) < int(min):
#             min =  minnumber[i]
#     return min

# print(find_min("1263405"))

#<=================================================================>
#ex4

# reversed string
# def reverse_string(string):
#     result = ""
#     last_index = len(string) -1
#     for i in range(len(string)):
#         result += string[last_index - i]
#     return result

# print(reverse_string("Good morning"))

#<=================================================================>
# counter string
# def count_string(string):
#     count_B = 0
#     count_A = 0
#     count_C = 0
#     for i in range(len(string)):
#         if string[i].lower() == "b":
#             count_B += 1
#         elif string[i].lower() == "a":
#             count_A += 1
#         elif string[i].lower() == "c":
#             count_C += 1

#     return count_A,  count_B, count_C
# print(count_string("banana"))
# print(count_string("apple"))
# print(count_string("coconut"))

#<=================================================================>
#find maximum

# def findMax(string):
#     max = 0
#     max = string[0]
#     for i in range(len(string)):
#         if int(string[i]) > int(max):
#             max = string[i]
#     return max

# print(findMax("122394848"))
# print(findMax("233321"))
# print(findMax("333444786"))

#<=================================================================>

# def getTotal(pluss):
#     sum = 0
#     for i in range(len(pluss)):
#         sum += int(pluss[i])
#     return sum
# print(getTotal("1234"))
# print(getTotal("4322"))    

#<=================================================================>

# def reverText(rever):
#     result = ""
#     last_index = len(rever) - 1
#     for i in range(len(rever)):
#         result += rever[last_index - i]
#     return result

# print(reverText("hello"))
# print(reverText("good morning"))
# print(reverText("world"))

#<=============================================>

# def countLetter(text, char):
#     counter = 0
#     for i in range(len(text)):
#         if text[i].lower() == char.lower():
#             counter += 1
#     return counter

# print(countLetter("banana", "a"))
# print(countLetter("boomb", "b"))
# print(countLetter("coconut", "c"))

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

# arr = [1, 2, 3, 4]
# for value in arr:
#     print("hello", str(value))

#<================================================>