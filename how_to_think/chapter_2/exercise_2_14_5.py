#get information
P = int(input("please give me the principal amount"))
r = int(input("please give me the annual nominal interest rate"))
n = int(input("please give me the number of times the interest is compounded per year"))
t = int(input("please give me the number of years"))

#calculations
A = ((P*(1+(r/n)))**(n*t))

#output
print(A)



