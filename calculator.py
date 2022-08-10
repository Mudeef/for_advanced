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
operator=input("Please choose an optional from these (1,2,3,4,5):")
print(operator)
if operator=="1":
    print("This is an Additional operation")
    print("This sum of the two number is :",num1+num2)
if operator=="2":
    print("This is an Subtraction operation")
    print("This difference of the two number is :", num1 - num2)
if operator=="3":
    print("This is an Multiplication operation")
    print("This product of the two number is :", num1 * num2)
if operator=="4":
    print("This is an Division operation")
    print("This  of the two number is :", num1 / num2)
if operator=="5":
    print("This is an Modulus operation")
    print("This  of the two number is :", num1 % num2)

