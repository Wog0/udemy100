




print("Welcome to the tip calculator!")
bill= float(input("what was the total bill? $"))
tip= int(input("How much tip would you like to give? 10, 12, or 15? "))
people= int(input("how many people should split the bill?"))

bill_tip_1= tip/100

bill_tip_2= bill * bill_tip_1

bill_tip_final= bill + bill_tip_2

total_split = round(bill_tip_final/ people, 2)

print(f"Each person should pay: {total_split}")
# tip_as_int = int(tip)
# bill_as_float= float(bill)
# split_as_int= int(split)

# bill_math= (tip_as_int/ bill_as_float)

# bill_math_continued = bill_as_float * bill_math

# bill_final = bill_as_float + bill_math_continued

# total_split = round(bill_final / split_as_int, 2)

# print(f"Each person should pay: {total_split}")


#bill_as_int=150
#tip_as_int= 12
#split_as_int =3



