import msvcrt


b = int(input("enter the second number: "))

print("to perform addition enter +: ")
print("to perform subtraction enter -: ")
print("to perform multiplication enter *: ")
print("to perform division enter /: ")
print("to perform power enter ^: ")

key = msvcrt.getch()
if key.decode() == '+':
    print("addition is ",a+b)
elif key.decode() == '-':
    print("subtraction is ",a-b)
elif key.decode() == '*':
    print("multiplcation is ",a*b)
elif key.decode() == '/':
    print("division is ",a/b)
elif key.decode() == '^':
    print("power is ",a**b)
else:
    print("invalid operator (^_^)")



def greeting():
    print("hello from calculator")
greeting()
def goodbye():
    print("good by and may you die ruthlessly")
goodbye()
def feature2():
    print("this is feature 2")
def feature1():
    print("this is a new feature")
feature1()
def feature5():
    print("hello from feature 5")
def feature4():
    print("hello from feature 4")

def feature6():
    print("hello from feature 6")