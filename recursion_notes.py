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
    
# def count_zoos(mystring):
#     if mystring == "":
#         return 0
#     if mystring[0] == "z":
#         return 1+count_zoos(mystring[1:])
#     else:
#         return 0+count_zoos(mystring[1:])
    
# letter=count_zoos("zigzag")
# print(letter)
# letter=count_zoos("Zigzag")
# print(letter)
# letter=count_zoos("zzzzzzzigzag")
# print(letter)
# letter=count_zoos("oooooohhhh")
# print(letter)

# def remove_space(my_string):
#     if my_string== "":
#         return ""
#     if my_string[0] ==" ":
#         return remove_space(my_string[1: ])
#     else:
#         return my_string[0] + remove_space(my_string[1:])
    
# string = remove_space( "v i n a y") 
# print(string)

## searching in list using recurstion 
# def is_item_in_list(my_list , target):
#     if target in my_list:
#         return True
#     else:
#         return False
# print(is_item_in_list([10,20,30,40], 20)) 

def is_item_in_list(mylist, target):
    if mylist== []:
        return False
    
    if mylist[0]==target:
        return True
    else:
        return is_item_in_list(mylist[1:], target)
    

print(is_item_in_list([10,20,30,40], 20))
print(is_item_in_list([10,20,30,40], 90))
    
