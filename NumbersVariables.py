print("Task One:Numbers & variables")
print("----------------------------")
print("Innovation_Python_YashMistry")
print("----------------------------")
print("----------------------------")

X= 123 ; Y= 24.05 ; Z=" Yash-MiStry" 

print(X, Y, Z)

print("2. Create a variable of value type complex and swap it with another variable whose value is an integer.")

Comp_num = 10 + 5j
print(Comp_num)

Int_num = 50
print(Int_num)

Int_num = 10 + 5j
print('the value after swap:', Int_num)


print("3. Swap two numbers using third variable as result name and do the same task without using any third variable.")

# swapping third variable as result name

num1 = input('Enter First number: ')

num2 = input('Enter Second number: ')

print("Value of num1 before swapping: ", num1)

print("Value of num2 before swapping: ", num2)

# using third variable as a result 

result = num1
num1 = num2
num2 = result

print("Value of num1 after swapping:", num1)
print("Value of num2 after swapping:", num2)

# without using third variable

num1 = input(' Please enter first Number:' )
num2 = input(' Please enter Second Number:')

print(" Value of num1 before swapping:", num1)
print(" Value of num2 before swapping:", num2)

#Swapping two numbers withouts any third variable

num1, num2 = num2, num1

print("value of num1 after swapping:", num1)
print("value of num2 after swapping:", num2)


#4. Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version.

#Python 2.x
#a= int(raw_inputb("Enter the value"))

#Python 3.x

b = input("Enter the value for python 3.x:")

Num1 = int(input("Enter first number between 1-10:"))
#Enter first number between 1-10:7
Num2 = int(input("Enter Second number between 1-10:"))
#Enter Second number between 1-10:5
z= Num1 + Num2
print(z)


z= z+30
print(z)


#6. Write a program to check the data type of the entered values. HINT: Printed output should say - The input value data type is : int/float/string/etc

p= 20.5

print( "The input value datatype is", type(p))
#The input value datatype is <class 'float'>

a= 'Yash'
print( "The input value datatype is", type(a))
#The input value datatype is <class 'str'>


a= 123
print( "The input value datatype is", type(a))

#The input value datatype is <class 'int'>


#7.Create Variable using CamelCase, LadderCase and UPPERCASE. (Refer: https://capitalizemytitle.com/camel-case/)

a="hello"
print(a.upper())


#8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change the value. If Yes then Why?

#Yes, value of varible a changes from one datatype to another datatype beacuse python is dynamic typed language. python will run code according datatype, python will stores the value at some memory location and collect names to that memory container. 






