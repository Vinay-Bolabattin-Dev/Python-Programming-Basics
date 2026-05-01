# # Movie Theater Pricing

# time = float(input("Enter a time(0-24)")) # 1=13 , 2=14, 3=15......

# age= int(input('Enter your age: '))

# if time<17:
#     print("Matinee Price: 100 rs")
# else:
#     if age <18 :
#         print("Evening youth price: 120 rs")
#     else:
#         print("Evenign Adult price: 150 rs")


## labrary Fine 

days_late = int(input("How many Days late is the Book??: "))


if days_late==0:
    print("No fine, Thank you!! ")
else:
    is_student= str (input("Are you student (yes or no ): "))

if is_student == "yes":
    fine = days_late * 5 
    print(f"Student Fine: {fine} rs")
else:
    fine = days_late * 10
    print(f"Standard Fine: {fine} rs")