# Challenge 1- Create a list and sort in ascending order

lines = "hello i am a list"

newlines = lines.split()
print(newlines)

lst = list() 

for line in newlines:
    lst.append(line)

lst.sort()
print(lst)

print("---------------------------")

#Challenge 2- Retrieve the largest number 

numbers = [43,89,67,56,12]

largestNum = max(numbers)

print(largestNum)

print("---------------------------")

#Challenge 3- Sum all the items in the list 

list_of_numbers = [10,20,30,40,50]

sumOfNum = sum(list_of_numbers)

print(sumOfNum)

print("---------------------------")

#Challenge 4- Remove duplicates from the following list 

list_of_dupes = [23, 45, 67, -10, 23, 50, -10]

newlist = list()

for dupe in list_of_dupes:
    if dupe not in newlist:
        newlist.append(dupe)

print(newlist)

print("---------------------------")

#Challenge 5- Create a loop through a list of numbers
#             Printing each element and its index

numList = list()

for counter in range(1, 11):
    numList.append(counter)
    print(F"{counter} {[counter - 1]}")

print(numList)

#Challenge 6- Create a tuple to store a student’s name, age, and grade

student = list()

studentInfo = {'name':'Paul', 'age': 20, 'grade': 'B +'}

for key, value in studentInfo.items():
        student.append(value)

print(tuple(student))

print("---------------------------")

#Challenge 7- Create a tuple that makes users 
#             choose an operator and perform basic calculations 
#             with two numbers.


chosenOperator = input("Please choose operator: +, -, *, /: ")    

try:
    num1 = int(input("Please enter a number: "))
except:
    print("Input was not an integer")

try:
    num2 = int(input("Please enter a number: "))
except:
    print("Input was not an integer")

mathOperators = ("+", "-", "*", "/")

if chosenOperator == mathOperators[0]:
    result = num1 + num2
elif chosenOperator == mathOperators[1]:
    result = num1 - num2 
elif chosenOperator == mathOperators[2]:
    result = num1 * num2 
elif chosenOperator == mathOperators[3]:
    result = num1 / num2 
else:
    print("Invalid operator")

try:
    print(result)
except:
    print("Something went wrong! ")

