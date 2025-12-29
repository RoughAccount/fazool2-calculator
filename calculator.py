import msvcrt

a = int(input("enter a number: "))
b = int(input("enter the second number: "))

print("to perform addition enter +: ")
print("to perform subtraction enter -: ")

key = msvcrt.getch()
if key.decode() == '+':
    print("addition is ",a+b)
elif key.decode() == '-':
    print("subtraction is ",a-b)
else:
    print("invalid operator (^_^)")