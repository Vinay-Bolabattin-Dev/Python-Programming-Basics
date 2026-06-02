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

def count_elements(my_list):
    if my_list==[]:
        return 0
    return 1+count_elements(my_list[1:])

iteams = count_elements([10,20,30,40])
print(iteams)
