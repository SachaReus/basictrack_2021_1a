#get information
principal_amount = int(input("please give me the principal amount"))
interest_rate = int(input("please give me the annual nominal interest rate"))
frequency_per_year = int(input("please give me the number of times the interest is compounded per year"))
number_of_years = int(input("please give me the number of years"))

#calculations
final_number = principal_amount * (1+(interest_rate/frequency_per_year)) ** (frequency_per_year*number_of_years)

#output
print(final_number)



