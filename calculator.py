replace1=""
flag="print"
print("*********  Welcome to the Zodiac calculator")
print("Enter the number1 :")
num1=int(input())
print("Enter the number2 :")
num2=int(input())
print(num2)
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.modulus")
result=0
operator=input("Please choose an optional from these (1,2,3,4,5):")
print(operator)
if operator=="1":
    replace1="Addition"
    result=num1+num2
if operator=="2":

    if num1<num2:
        flag="Do not print"
        print("Cannot subtract the First number is less then the Second number")
    else:
        flag="print"
        replace1="Subtraction"
        result=num1-num2
if operator=="3":
    replace1="Multiplication"
    result=num1*num2
if operator=="4":
    replace1="Division"
    result= num1//num2
if operator=="5":
    replace1="Modulus"
    result=num1%num2
if flag=="Print":
    print("The result of",replace1,"of",num1,"and",num2,"is",result)

