# write a program to print factorial of a given number?
# e.g: 5 = 5 x 4 x 3 x 2 x 1 = 120

i = int(input('Enter a number: '))           # i = 5 
fact = 1
while (i>0):
    fact = fact * i                         #  ( 1 x 5 = 5 )
    i = i - 1                               # 5 - 1 = 4
print("Factorial of the number is: ", fact)