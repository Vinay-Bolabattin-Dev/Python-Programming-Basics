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

# def is_item_in_list(mylist, target):
#     if mylist== []:
#         return False
    
#     if mylist[0]==target:
#         return True
#     else:
#         return is_item_in_list(mylist[1:], target)
    

# print(is_item_in_list([10,20,30,40], 20))
# print(is_item_in_list([10,20,30,40], 90))
    
# def divide_list(my_list):

#     if len(my_list) <=1:
#         return my_list
    
#     mid = len(my_list) //2
#     left = my_list[ :mid]
#     right=my_list[mid:]

#     print(f"splitting: left ={left}, right={right}")

#     divide_list(left)
#     divide_list(right)


# number= divide_list([10,11,12,13,14,15,16])


# def count_spliting(my_list):
#     if len(my_list)<=1:
#         return 0
    

#     mid =len(my_list) //2
#     left = (my_list)[:mid]
#     right=(my_list)[mid: ] 


#     return 1 + count_spliting(left) + count_spliting(right)

# total_value=count_spliting([10,11,12,13,14,15,16])
# print(f'total splite {total_value}')
    

# def count_dacteria(hours):
#     if hours==0:
#         return 1
    
#     if hours >0:
#        return  2 * count_dacteria(hours-1)
    
    
    
# print(count_dacteria(5))


# def count_steps_taken(total_steps):
#     if total_steps == 0:
#         return 0
    
#     return 


# def has_character(my_string, target):

#     if my_string== "":
#         return False
    
#     if my_string[0]==target:
#         return True
#     else:
#        return has_character(my_string[1:], target)

# print(has_character("vinay", "a"))  # Should print True
# print(has_character("solapur", "z")) # Should print False

# def has_vowel(mystring, target=['a','e','i','o','u']):
#     if mystring== "":
#         return False
    
#     if mystring[0] in target :
#         return True
#     else:
#         return has_vowel(mystring[1:])
    
# print(has_vowel("rhythm"))  # Should print False
# print(has_vowel("solapur")) # Should print True

# def count_evens(mylist):
#     if mylist== []:
#         return 0
    
#     if mylist[0] % 2==0:
#         return 1 + count_evens(mylist[1: ])
#     else:
#         return count_evens(mylist[1:])
# print(count_evens([2, 5, 4, 7, 8]))  # Should print 3 (because 2, 4, and 8 are even)
# print(count_evens([1, 3, 5, 7, 9]))  # Should print 0

# def Divide_list(mylist):
#     if len(mylist) <=1:
#         return mylist

#     mid = len(mylist) //2

#     left_half= mylist[ :mid]
#     right_half=mylist[mid: ]

#     print(f"Spliting: left half= {left_half} & Right half = {right_half}")

#     Divide_list(left_half)
#     Divide_list(right_half)

# Divide_list([38, 27, 43, 3])

# def replace_spaces(my_string):
#     if my_string== "":
#         return ""
    
#     if my_string[0]==" ":
#         return "-" + replace_spaces(my_string[1: ])
#     else: 
#         return my_string[0] + replace_spaces(my_string[1: ])
# print(replace_spaces("v i n a y"))  # Should print "v-i-n-a-y"
# print(replace_spaces("solapur city")) # Should print "solapur-city"


# def add_exclamation(my_string):
#     if my_string=="":
#         return ""
    
#     if my_string[0] =='a':
#         return "a!" + add_exclamation(my_string[1: ])
#     else:
#         return my_string[0] + add_exclamation(my_string[1: ])
    
# print(add_exclamation("vinay")) # Should print "vina!y"
# print(add_exclamation("banana")) # Should print "ba!na!na!"

# def remove_x(my_string):
#     if my_string=="":
#         return ""
    
#     if my_string[0]=='x':
#         return '' + remove_x(my_string[1: ])
#     else:
#         return my_string[0] + remove_x(my_string[1: ])
    
# print(remove_x("axbxidxexk")) # Should print "abidek"
# print(remove_x("xbox"))       # Should print "bo"

# def flatten_list(nested_list):
#     if nested_list==[]:
#         return []
    
#     if isinstance(nested_list[0], list ):
#         return flatten_list(nested_list[0]) + flatten_list(nested_list[1: ])
#     else:
#         return [nested_list[0]] + flatten_list(nested_list[1:])

# print(flatten_list([1, [2, 3], 4]))    # Should print [1, 2, 3, 4]
# print(flatten_list([[1, 2], [3, 4]]))  # Should print [1, 2, 3, 4]

# def multiply_chars(my_string, n ):

#     if my_string=="":
#         return ''
#     return (my_string[0] * n) + multiply_chars(my_string[1:],n)


# print(multiply_chars("abc", 3))   # Should print "aaabbbccc"
# print(multiply_chars("vinay", 2)) # Should print "vviinnaayy"

# def is_sorted(mylist):
#     if len(mylist)<=1:
#         return True
    
#     if mylist[0] > mylist[1]:
#         return False
    
#     return is_sorted(mylist[1: ])
# print(is_sorted([1, 3, 5, 8]))  # Should print True
# print(is_sorted([1, 7, 5, 9]))  # Should print False (because 7 is greater than 5)
        
    
# def find_index(mylist, target , current_idx=0):
#     if mylist==[]:
#         return -1
    
#     if mylist[0]==target:
#         return current_idx
#     else:
#         return find_index(mylist[1:], target, current_idx + 1)
    
# print(find_index([10, 20, 30, 40], 30))  # Should print 2
# print(find_index([10, 20, 30, 40], 99))  # Should print -1

def power(base, exponent):
    if exponent==0:
        return 1
    
    return base*power(base,exponent -1 )
print(power(2, 3))  # Should print 8  (2 * 2 * 2)
print(power(5, 2))  # Should print 25 (5 * 5)
print(power(7, 0))  # Should print 1  (Any number to the power of 0 is 1)