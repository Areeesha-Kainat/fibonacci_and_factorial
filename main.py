# write a program to print fibonacci series upto a given number?

# pehle 2 numbers 0 or 1 ko add krke jo answer aega wo 3rd number hoga
# 0 + 1 = 1  ko add krke jo answer aega wo 2 hoga
# 1 + 1 = 2  ko add krke jo answer aega wo 3 hoga
# 1 + 2 = 3  ko add krke jo answer aega wo 4 hoga
# 2 + 3 = 5  ko add krke jo answer aega wo 5 hoga
# 3 + 5 = 8  ko add krke jo answer aega wo 6 hoga

# start hamesha 0 or 1 se krte hai or agla number in dono ko sum krke ata hai

n = int(input("Enter a number: "))              # n = 10
x = 0
y = 1
z = 0
while z <= n:                                   # check kro z is less than or equal to n
    print(z)
    x = y                                       # y ki value x men daldo (x=1)
    y = z                                       # z ki value y men daldo (y=0)
    z = x + y                                   # z = x + y  (1+0=1)

    # phir wapis condition check karega (z men 1 hai n men 10)   1 jo hai wo 10 se chota hai ya baraber 




