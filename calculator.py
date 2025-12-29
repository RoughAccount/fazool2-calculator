import msvcrt

a = int(input("enter a number: "))
b = int(input("enter the second number: "))

print("to perform addition enter +: ")

key = msvcrt.getch()
if key.decode() == '+':
    print("addition is ",a+b)