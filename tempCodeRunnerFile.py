# def find_factorial(n):
#     # if n ==1:
#     #     return 1
    
    
#     return n*find_factorial(n-1)
# result=find_factorial(4)
# print(f"Factorial is {result}")

## practically example 
## 1.1
# def count_up(num):
#     if num==0:
#         return 
#     count_up(num-1)
#     print(num)

# number = count_up(10)

## 1.2
# def calculate_sum(n):
#     if n==1:
#         return 1
#     return n+calculate_sum(n-1)

# num= calculate_sum(4)
# print(num)

## 1.3 

# def count_elements(my_list):
#     if my_list==[]:
#         return 0
#     return 1+count_elements(my_list[1:])

# iteams = count_elements([10,20,30,40])
# print(iteams)


# def multiply_all(my_list):
#     if my_list ==[]:
#         return 1
#     return my_list[0] * multiply_all(my_list[1: ])

# num=multiply_all([2, 3, 5])
# print(num)


# def count_letters(my_string):
#     if my_string == "":
#         return 0 
    
#     return 1 + count_letters(my_string[1:])

# result=count_letters("hi")
# print(result)
    
def count_zoos(mystring):
    if mystring == "":
        return 0
    if mystring[0] == "z":
        return 1+count_zoos(mystring[1:])
    else:
        return 0+count_zoos(mystring[1:])
    
letter=count_zoos("zigzag")
print(letter)
letter=count_zoos("Zigzag")
print(letter)
letter=count_zoos("zzzzzzzigzag")
print(letter)
letter=count_zoos("oooooohhhh")
print(letter)