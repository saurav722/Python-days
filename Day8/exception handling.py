print('H')
#print(10/0)   //show error in code thats why we write it in try block
try:
    a=10
    print(a/2)
except ZeroDivisionError as z:
    print('z')
else:
    print('Hello')
finally:
    print('This is finally executed..')