# # # # # # # # # # # # # # # # # # Movie Theater Pricing

# # # # # # # # # # # # # # # # # time = float(input("Enter a time(0-24)")) # 1=13 , 2=14, 3=15......

# # # # # # # # # # # # # # # # # age= int(input('Enter your age: '))

# # # # # # # # # # # # # # # # # if time<17:
# # # # # # # # # # # # # # # # #     print("Matinee Price: 100 rs")
# # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # #     if age <18 :
# # # # # # # # # # # # # # # # #         print("Evening youth price: 120 rs")
# # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # #         print("Evenign Adult price: 150 rs")


# # # # # # # # # # # # # # # # ## labrary Fine 
# # # # # # # # # # # # # # # days_late = int(input("How many Days late is the Book??: "))


# # # # # # # # # # # # # # # if days_late==0:
# # # # # # # # # # # # # # #     print("No fine, Thank you!! ")
# # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # #     is_student= str (input("Are you student (yes or no ): "))

# # # # # # # # # # # # # # #     if is_student =="yes":
# # # # # # # # # # # # # # #         fine= days_late *5
# # # # # # # # # # # # # # #         print(f"Student Fine: {fine} rs")
# # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # #         fine=days_late * 10
# # # # # # # # # # # # # # #         print(f"Standered Fine: {fine} rs")



# # # # # # # # # # # # # # # """ String 
# # # # # # # # # # # # # # # practice + Revision  """

# # # # # # # # # # # # # # # movie_name = "2026_PROJECT_CLIP_01.MP4"


# # # # # # # # # # # # # # # movie_name.strip() # removing extra space 

# # # # # # # # # # # # # # # movie_name[0:5] # printing only year from name 

# # # # # # # # # # # # # # # movie_name.replace("CLIP", "SCENE") # replacing clip to scene 

# # # # # # # # # # # # # # # final_moviename= movie_name.lower()
# # # # # # # # # # # # # # # print(final_moviename)


# # # # # # # # # # # # # # # ## List 
# # # # # # # # # # # # # # # assets = ["intro", "vlog_clip", "outro"]


# # # # # # # # # # # # # # # assets[1 ]= "cinematic_shot"

# # # # # # # # # # # # # # # assets.append("Background_music")

# # # # # # # # # # # # # # # assets.sort()
# # # # # # # # # # # # # # # print(assets)

# # # # # # # # # # # # # # # ## slicing in list 
# # # # # # # # # # # # # # # a= assets[0:2]
# # # # # # # # # # # # # # # print(a)

# # # # # # # # # # # # # # ## TUPLES
# # # # # # # # # # # # # # #Example 1
# # # # # # # # # # # # # # # required_resolution=(1970, 1080)
# # # # # # # # # # # # # # # width=int(input('Enter a width: '))
# # # # # # # # # # # # # # # height= int (input("Enter a height: "))

# # # # # # # # # # # # # # # if width == required_resolution[0] and required_resolution[1]:
# # # # # # # # # # # # # # #     print("Resolution Match! Ready to export")

# # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # #     print("Warning: Resolution mismatch.")

# # # # # # # # # # # # # # #example 2:

# # # # # # # # # # # # # # # peack_hours=(10,14, 20) #(representing 10 AM, 2 PM, and 8 PM).

# # # # # # # # # # # # # # # post_time= int(input("Enter you post time: "))

# # # # # # # # # # # # # # # if post_time == peack_hours[0] or post_time== peack_hours[2]:
# # # # # # # # # # # # # # #     print("Excellent timing! High engagement expected")
# # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # #     print("standard post time ")


# # # # # # # # # # # # # # # """ Dictionary """

# # # # # # # # # # # # # # # #creating a Dictionary 

# # # # # # # # # # # # # # # mi_player ={
# # # # # # # # # # # # # # #     "name":"Rohit sharma",
# # # # # # # # # # # # # # #     "team":"Mumbai Indians",
# # # # # # # # # # # # # # #     "runs": 105 ,
# # # # # # # # # # # # # # #     "lat_five_score": [105,10,36,0,11],
    
# # # # # # # # # # # # # # #     "squad":{ 
# # # # # # # # # # # # # # #         "player_name": ["Rohit", "ishan", "Hardik", "Surya"]
    

# # # # # # # # # # # # # # #     },
# # # # # # # # # # # # # # #     "unique_team":{"MI",'MI', "CSK"}

    

# # # # # # # # # # # # # # # }

# # # # # # # # # # # # # # # # print(mi_player["lat_five_score"][-1])
# # # # # # # # # # # # # # # # print(mi_player.keys())
# # # # # # # # # # # # # # # # print(mi_player.get("team"))
# # # # # # # # # # # # # # # print(mi_player["squad"]["player_name"])  
# # # # # # # # # # # # # # # mi_player["squad"]["player_name"].append("Bumarah")
# # # # # # # # # # # # # # # # print(mi_player["squad"].values())
# # # # # # # # # # # # # # # mi_player["squad"]["player_name"].append("Rohit")
# # # # # # # # # # # # # # # print(mi_player["squad"]["player_name"])
# # # # # # # # # # # # # # # print(mi_player.get("unique_team"))

# # # # # # # # # # # # # # ## SET 

# # # # # # # # # # # # # # mi_squad ={"Rohit", "Bumrah", " Hardik", "Sky"}

# # # # # # # # # # # # # # indian_squad={"Gill", "Sanju", "Rohit", "Bumrah", 'Virat', "Sky"}

# # # # # # # # # # # # # # print(mi_squad.union(indian_squad))

# # # # # # # # # # # # # # mi_squad.add("Tilak")
# # # # # # # # # # # # # # print(mi_squad)
# # # # # # # # # # # # # # print(mi_squad.intersection(indian_squad))
# # # # # # # # # # # # # # indian_squad.clear()
# # # # # # # # # # # # # # print(indian_squad)


# # # # # # # # # # # # # ## Loops  

# # # # # # # # # # # # # # count =1
# # # # # # # # # # # # # # total_sum =0
# # # # # # # # # # # # # # while count <=5:
# # # # # # # # # # # # # #     total_sum+=count
# # # # # # # # # # # # # #     count +=1
# # # # # # # # # # # # # # print(total_sum)

# # # # # # # # # # # # # num=1
# # # # # # # # # # # # # factorial=1
# # # # # # # # # # # # # while num<=5:
# # # # # # # # # # # # #     factorial=factorial*num
# # # # # # # # # # # # #     num+=1
# # # # # # # # # # # # # print(factorial)

# # # # # # # # # # # # # num=1
# # # # # # # # # # # # # while num <=15:
# # # # # # # # # # # # #     if num %2!=0:
# # # # # # # # # # # # #         print(num)
# # # # # # # # # # # # #     num +=1

# # # # # # # # # # # # # ## Divided by 3
# # # # # # # # # # # # # number =1
# # # # # # # # # # # # # while number <=20:
# # # # # # # # # # # # #     if number % 3 ==0:
# # # # # # # # # # # # #         print(number)
# # # # # # # # # # # # #     number+=1

# # # # # # # # # # # # # ##print 1 to 10 but skip 7 
# # # # # # # # # # # # # n=0
# # # # # # # # # # # # # while n <=10:
# # # # # # # # # # # # #     n +=1
# # # # # # # # # # # # #     if n==7:
# # # # # # # # # # # # #         continue
# # # # # # # # # # # # #     print(n)


# # # # # # # # # # # # # ##string loop
# # # # # # # # # # # # # code =""
# # # # # # # # # # # # # while code !="MI": 
# # # # # # # # # # # # #     code= str (input ("Enter a vaild code for access: "))
# # # # # # # # # # # # #     if code == "MI":
# # # # # # # # # # # # #         print("Access Granted! Go ahead!")
# # # # # # # # # # # # #     else:
# # # # # # # # # # # # #         print("Not valid code")
    
# # # # # # # # # # # # # count=1
# # # # # # # # # # # # # while count<=20:
# # # # # # # # # # # # #     if count %5==0:
# # # # # # # # # # # # #         print(count)
# # # # # # # # # # # # #     count +=1

# # # # # # # # # # # # ##list loops
# # # # # # # # # # # # players = ["Rohit", "Surya", 'Tilak' , "Hardik", "Bumrah"]
# # # # # # # # # # # # index=0
# # # # # # # # # # # # while index < (len(players)):
# # # # # # # # # # # #     if players[index] =="Hardik":
# # # # # # # # # # # #         break
# # # # # # # # # # # #     print(players[index])
# # # # # # # # # # # #     index +=1

# # # # # # # # # # # ##hard question 
# # # # # # # # # # # # index=0
# # # # # # # # # # # # total_score=0

# # # # # # # # # # # # while index < len(runs):
# # # # # # # # # # # #     if runs[index] ==0:
# # # # # # # # # # # #         index +=1
# # # # # # # # # # # #         continue
# # # # # # # # # # # #     total_score+=runs[index]
# # # # # # # # # # # #     index +=1

# # # # # # # # # # # # print(f"total sore: {total_score}")

# # # # # # # # # # # ##advanced question 
# # # # # # # # # # # # match_scores = [15, 48, 22, 96, 10, 35]
# # # # # # # # # # # # index = 0
# # # # # # # # # # # # big_hits = 0
# # # # # # # # # # # # small_scores = 0

# # # # # # # # # # # # while index < len(match_scores):
# # # # # # # # # # # #     if match_scores[index]>=30:
# # # # # # # # # # # #         big_hits +=1
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         small_scores +=1
# # # # # # # # # # # #     index +=1
# # # # # # # # # # # # print(f"total number of big hits {big_hits} & small scores {small_scores}")

# # # # # # # # # # # # prices = [120, 450, 0, 890, 300]
# # # # # # # # # # # # index = 0

# # # # # # # # # # # # while index < len(prices):
# # # # # # # # # # # #     if prices[index]==0:
# # # # # # # # # # # #         prices[index]=500
# # # # # # # # # # # #         print(f"Fount the error at the {index}, updated it with {prices[index]}")
# # # # # # # # # # # #         break
    
# # # # # # # # # # # #     index +=1
# # # # # # # # # # # # print(prices)
    
# # # # # # # # # # # """ FOR  
# # # # # # # # # # #    LOOPS 
# # # # # # # # # # # Question practice / revision  """
# # # # # # # # # # # # Ex:1 
# # # # # # # # # # # # number=[1,2,3,4,5]

# # # # # # # # # # # # for num in number:
# # # # # # # # # # # #     print(num*10)

# # # # # # # # # # # # # Ex:2
# # # # # # # # # # # # scores = [25, 60, 45, 90, 30, 100]
# # # # # # # # # # # # for n in scores:
# # # # # # # # # # # #     if n>=50:
# # # # # # # # # # # #         print(n)

# # # # # # # # # # # #Ex:3
# # # # # # # # # # # runs = [40, 10, 50, 0, 20]
# # # # # # # # # # # total = 0
# # # # # # # # # # # for i in runs:
# # # # # # # # # # #     total+=i
# # # # # # # # # # # print(total)

# # # # # # # # # # ## Range()
# # # # # # # # # # # for i in range(1,11):
# # # # # # # # # # #     print(i)


# # # # # # # # # # # for table in range(1,11):
# # # # # # # # # # #     print(f"5*{table}")
# # # # # # # # # # # or 
# # # # # # # # # # # for table in range(5,55,5):
# # # # # # # # # # #     print(table)

# # # # # # # # # # # players = ["Rohit", "Surya", "Tilak", "Hardik"]

# # # # # # # # # # # for i in range (len(players)):
# # # # # # # # # # #     print(f"Rank {i}:{players[i]}")

# # # # # # # # # # ## Print only the players who are at an even rank or index using [range(),for loop and if logic]
# # # # # # # # # # # players = ["Rohit", "Surya", "Tilak", "Hardik", "Bumrah"]

# # # # # # # # # # # for i in range ((len(players))):
# # # # # # # # # # #     if i %2==0:
# # # # # # # # # # #         print(players[i])

# # # # # # # # # # ## Print only the players who are at an even rank or index using range()
# # # # # # # # # # players = ["Rohit", "Surya", "Tilak", "Hardik", "Bumrah"]
# # # # # # # # # # for i in range(0,len(players),2):
# # # # # # # # # #     print(i,players[i])

# # # # # # # # # ## Nested Loops 
# # # # # # # # # for i in range (1,3):
# # # # # # # # #     for j in range (1,4):
# # # # # # # # #         print(f"Row {i} , Column {j}")


# # # # # # # # for i in range(1,4):
# # # # # # # #     for j in range (1,4):
# # # # # # # #         print("*" ,end=" ")
# # # # # # # #     print() # to move next line 

# # # # # # # # rows=["A", "B"]
# # # # # # # # for r in rows:
# # # # # # # #     print(f"Row {r}:", end=" ")
# # # # # # # #     for s in range(1,4):
# # # # # # # #         print(s, end=" ")
# # # # # # # #     print()

# # # # # # # # all_teams = [
# # # # # # # #     [10, 20, 30], # Team 1
# # # # # # # #     [40, 50, 60]  # Team 2
# # # # # # # # ]
# # # # # # # # for team in all_teams:
# # # # # # # #     for score in team:
# # # # # # # #         print(score)

# # # # # # # ###Pattern  printing by using loops 
# # # # # # # # for i in range(1,6):
# # # # # # # #     print(end=" ")
# # # # # # # #     for j in range(i):
# # # # # # # #         print("*", end="")
# # # # # # # #     print()

# # # # # # # # size = int(input("Enter a Traingel size to print: "))
# # # # # # # # for i in range(1,size+1):
# # # # # # # #     for j in range (i):
# # # # # # # #         print("*", end="")
# # # # # # # #     print()

# # # # # # # # size = int(input("Enter a Traingel size to print: "))
# # # # # # # # for i in range(size, 0 , -1):
# # # # # # # #     for j in range (i):
# # # # # # # #         print("*", end="")
# # # # # # # #     print()

# # # # # # # size = int(input("Enter a Traingel size to print: "))

# # # # # # # for i in range(1,size+1):
# # # # # # #     for j in range (i):
# # # # # # #         print("#", end="")
# # # # # # #     print()

# # # # # # # for i in range(size-1,0,-1):
# # # # # # #     for j in range(i):
# # # # # # #         print("#", end="")
# # # # # # #     print()


# # # # # # # size= int (input("Enter a size: "))
# # # # # # # symbol= input("Enter a symbol:")

# # # # # # # for i in range(1,size+1):
# # # # # # #     for j in range(i):
# # # # # # #         print(f"{symbol}", end="")
# # # # # # #     print()

# # # # # # size= int (input("Enter a size: "))
# # # # # # symbol= input("Enter a symbol:")

# # # # # # for i in range(1,size+1):
# # # # # #     for j in range(i):
# # # # # #         print(f"{symbol}", end="")
# # # # # #     print()
# # # # # # for i in range(size-1,0, -1):
# # # # # #     for j in range(i):
# # # # # #         print(f"{symbol}", end="")
# # # # # #     print()


# # # # # ## Pass statemnt :
# # # # # """" pass statement is a null statement that does nothing,
# # # # # just used to work placeholder for future code 
# # # # # Ex: """
# # # # # def game_over():
# # # # #     #I'll finish tomorrow!
# # # # #     pass

# # # # ###FUNCTIONS 

# # # # def sum(num):
# # # #     print(num+num+num)
# # # #     return 
# # # # #sum(10)

# # # # def A(symbol, number):
# # # #     print(symbol*number)
# # # #     return 
# # # # A("@",5)

# # # # def float_square(size, char):
# # # #     for i in range(size+1):
# # # #         for j in range(size):
# # # #             print(f"{char}", end="")
# # # #         print()

# # # # #float_square(5, "@")

# def reverse_trangle(size, char):
#     for i in range(size+1,0,-1):
#         for j in range(i):
#             print(f"{char}", end="")
#         print()
# reverse_trangle(4,"!")

# # ### parameter function 
# # # # def describe_item(name, color):
# # # #     print(f'This is {name} and its in {color}color')

# # # # describe_item("Laptop", "Silver")

# # # # defualt function
# # # def set_volume(level=50):
# # #     print(f"value set to {level}%")
# # # set_volume(80)
# # # set_volume()

# # # ## Return function 
# # # def get_half(number):
# # #     return number /2
# # # my_nane=get_half(100)
# # # print(my_nane)

# # def calculate_total(price, qty):
# #     return price*qty
# # def apply_discount(total):
# #     return total-10
# # bill=calculate_total(100 ,5)
# # final_bill=apply_discount(bill)
# # print(final_bill)

# ##combine Functions, Returns, and If/Else.
# def check_stock(avaliable, ordered ):
#     if ordered<=avaliable:
#         return "Order Successful"
#     else:
#         return "Out of stock "
    
# print(check_stock(10,5))
# print(check_stock(10,50))


# # warm up challenge "Full project" shop management

# def final_checkout(price ,quantity, stock_available):
#     if quantity>=stock_available:
#         return "Transection failed : Not enough stock "
#     total=price*quantity
#     if total>=500:
#         total=total-50
        
#     return total

# print(final_checkout(200, 3, 10))
# print(final_checkout(100, 10, 5))

## example for stock check         
# products={
#     "laptop": 50000,
#     "Mouse": 1500,
#     "Monitor":2000,
# }

# def stock_check(product):
#     if product in products:
#         print(f"Yes it is in stock, price: {products[product]}")
#     else:
#         print("Sorry!! Out of Stock")

# # stock_check("Mouse")
# # stock_check("Tv")

# def get_final_price(product, quantity):
#     if product in products:
#         total= products[product]* quantity
#         return total 
#     else:
#         return 0 
# bill= get_final_price("Monitor", 3)
# print(bill)

""" FILE 
Input and Out """

# with open("log.txt", "w") as f:
#     f.write("Day 11: I am learning File I/O today ")

   

# with open("log.txt", "a") as  f:
#     f.write("\nThis is 2nd line of m")

# f= open("log.txt", "r")
# data=f.read()
# print(data)

# f.close()

# def find_word(target):
#     with open("log.txt","r") as f:
#         data=f.read()
#         if target in data:
#             print(f" {target}word Found")
#         else:
#             print(f"{target} Not found")
#         new_data=data.replace("m", "My practice or lerning ")
    
#     with open("log.txt", "w") as f :
#         f.write(new_data)
#         print("File is Updated with new data ")
#         return new_data
# result=find_word("Python")
# print(result)


# with open("data.txt", "w") as f:
#     f.write("10,20,30,40,50")

# with open('data.txt', "r") as f:
#     folder=f.read()
#     print(folder)

# my_list=folder.split(",")
# print(my_list)


# with open ("user_info.txt", 'a') as f:
#     name= str(input("Enter your name: "))
#     f.write(name+"\n")
    
# with open("user_info.txt", "r") as f:
#     data=f.read()
#     print(f"total Numbers of characters: {len(data)}")

# with open("prices.txt", "w")as f:
#     f.write("1500,2000,500,3000,450")

# with open("prices.txt", "r") as f:
#     rates=f.read()
#     new_data= rates.split(",")
#     # print(new_data)
#     int_prices=[]
#     for p in new_data:
#         int_prices.append(int(p))
#         print(p)
#     print(f"The Highest price is:{max(int_prices)}")
   
# with open("inventory.txt", "w") as f:
#     f.write("laptop:50000\nmouse:1500\nmonitor:6000")
    
# with open("inventory.txt", "r") as f:
#     lines=f.readlines()
    
#     for line in lines:
#         parts= line.strip().split(":")

#         name=parts[0]
#         price=int(parts[1])

#         if price >2000:
#             print(f"{name} is a premium iteam (price:{price})")
#         else:
#             print(f"{name} is a budget iteam (price:{price})")
        
      
# with open("users.txt", "w") as f:
#     f.write("admin:1234\nuser1:pass1\narjun:7890")
#     user_input=input("Enter username: ")
#     found=False
# with open("users.txt","r") as f:
    
#     for line in f:
#         parts=line.strip().split(":")
        
#         if parts[0]==user_input:
#             found= True
#             break
# if found:
#     print("Access Granted !!")
# else:
#     print("Acces not Granted!!")


# with open("scores.txt", "w") as f :
#     f.write("Rahul:45\nDeepak:82\nSagar:91\nKiran:30")

# with open("scores.txt", "r") as f:

#     for line in f:
#         parts=line.strip().split(":")

#         name=parts[0]
#         scores=int(parts[1])
    
#         if scores>80:
#             print(f"Name: {name}||Runs scored: {scores}")

# with open("account.txt", "w") as f:
#     f.write("5000")

# with open("account.txt", "r") as f:
#     balance=int(f.read())
#     print(f'Current Balance: {balance}')
#     chiose = input("Do you want to (W)ithdrwa or (D)iposit? ").upper()
#     ammount= int(input("Enter you ammount"))

#     if chiose=="D":
#         balance=balance+ammount
#     elif chiose=="W":
#         if ammount<=balance:
#             balance = balance-ammount
#         else:
#             print("Insufficient Ammount !! ")
#     print(f'Updated total balance:{balance}')
# with open("account.txt", "w") as f:
#     f.write(f"Your Current Balance\n{balance}")

# f.close

"""" Exception Handling 
by using (try, except , else and finally blocks )"""

# ##practice
# try:
#     number=int(input("Enter a number to divide 100: "))
#     result=100/number
#     print(f'Success!! The answers is {result}')

# except ValueError:
#     print("Logic Error: You typed a word , but i needed number!!")

# except ZeroDivisionError:
#     print("math error: you can't divide by 0!! the universe will exloade ")

# print("program is still running!! it did't crash ")


# try:
#     a=int(input("Enter 1st num:"))
#     b=int(input("Enter 2nd num: "))
#     result=a/b
#     result_wholenum=a//b
#     print(f'Divistion of two number is:{result} in whole number:({result_wholenum})')

# except ValueError:
#     print("I need number not a characters")

# except ZeroDivisionError:
#     print("math error: you cant divide by 0 ")

# finally:
#     print("code executed ")

## excpetion handling on files 
# try:
#     with open ('database.txt', "r") as f:
#         pass
# except FileNotFoundError:
#     print("file not found!! Creating it now")

#     with open("database.txt", "w") as f:
#         f.write("this is new file")
        
# finally :
#     print("file check has been completed ")


## make ATM bullet proof by excpetion handling 
# balance=0
# try:
#     with open("account.txt", "r") as f:
#         content=f.read()
#         if content:
#             balance=int(content)
        
# except FileNotFoundError:
#     print("File not Found or missing !! creating a new account with 5000 ")
#     balance=5000
#     with open("account.txt", "w") as f:
#         f.write(str(balance))
# try:
#     print(f'Current Balance:{balance}')
#     chiose = input("Do you want to (W)ithdrwa or (D)iposit? ").upper()
#     ammount= int(input("Enter you ammount"))
        
#     if chiose=="D":
#         balance=balance+ammount
#     elif chiose=="W":
#         if ammount<=balance:
#             balance = balance-ammount
#         else:
#             print("Insufficient Ammount !! ")
#     else:
#         print("Invalid choise!! please select w or d ")

#     with open("account.txt", "w") as f:
#         f.write(str(balance))

#         print(f"your updated balance:{balance}")
# except ValueError:
#     print("Enter number for a ammount and proper character out of (W)ithdrwa or (D)iposit at chiose")

# finally:
#     print("-------------------------------------------")
#     print("thank you for using ATM, Hope to see u soon")
#     print("____________________________________________")


# f.close

"""" OOPs (Object oriented programming)
Class & Object and Contructor(__init__)"""

# class student:
#     def __init__(self, name , rollnumber, marks):
#         self.name=name
#         self.roll_no=rollnumber
#         self.marks=marks
#     college_name="DBF college"

#     def display(self):
#         print(f'Student name is {self.name} & roll number:{self.roll_no}')

#     def check_result(self):
#         if self.marks>33:
#             print("PASSED")
#         else:
#             print("Failed")

#     def update_marks(self,new_marks):
#         self.marks=new_marks

#     def get_percentage(self,total_marks):
#         percentage = (self.marks /total_marks)*100
#         print(f"Percantage:{percentage}%")
      
#     def Full_report(self, total_marks):
#         self.display()
#         self.get_percentage(total_marks)
#         self.check_result()
        
        
# classroom=[
#     student("A",1,90), 
#     student("B",2,30), 
#     student("C", 3,45),
# ]
# for s in classroom :
#     s.Full_report(100)
#     print("-"*20)


    
# classroom[1]

## Inheritance 
""" Type mo:1 
single inheritance """

# class Animal:
#     def __init__(self, name):
#         self.name=name
#         print(f"This is my animal name:{self.name}")
    
#     def eat(self):
#         print(f"{self.name} is Eating....")

# class Dog(Animal):
#     def __init__(self,name):
#         super().__init__(name)
            
#     def bark(self):
#         print(f"{self.name} is barking, Woof!!")

# p1=Dog("Rocky")
# p1.eat()
# p1.bark()
# p2=Animal("Charly")
# p2.eat()

# class Employee:
#     def __init__(self, name , Salary):
#         self.name=name
#         self.Salary=Salary
#     def show_details(self):
#         print(f"Employee name is {self.name} and his salary is :{self.Salary}")

# class Developer(Employee):
#     def __init__(self,name, Salary, language):
#         super().__init__(name, Salary)
#         self.language=language

#     def show_details(self):
#         super().show_details() #overriding 
#         print(f"he works by using {self.language} language")

# Emp1=Developer("vinay", 500000, "Python")
# Emp1.show_details()

# class account :
#     def __init__(self, holder_name, balance):
#         self.holder_name=holder_name
#         self.balance=balance

#     def view_current_balance(self):
#         print(f"The Current Balance is {self.balance}")

# class Saving_Account(account):
#     def __init__(self, holder_name, balance):
#         super().__init__(holder_name, balance)

#     def add_intereset(self,rate):
#         if self.balance>500:
#            self.balance=self.balance*rate/100
#            print(f"Interest added,new_balance={self.balance}")
#         else:
#             print("insufficent balance for interest ")

# s1=Saving_Account("vinay",2000)
# s1.add_intereset(5)
# s1.view_current_balance

# s2=Saving_Account("B", 10000)
# s2.add_intereset(5)

## Method Overriding in python :

# class shape:
#     def draw(self):
#         print("Drawing a generic shape")

# class cricle(shape):
#     def draw(self):
#         print("Drawing Cricle ")

# c1=cricle()
# c1.draw()

# class emial:
#     def __init__(self, reciver):
#         self.reciver=reciver
    
#     def send(self):
#         print(f"Email sent to {self.reciver}")

# class secureEmail(emial) :
#     def send(self):
#         print("Ebcription enabled... ")
#         super().send()

# e1=secureEmail("vinay")
# e1.send()

## Discount system
# class product:
#     def __init__(self, name , price):
#         self.name=name
#         self.price=price
    
#     def display_info(self):
#         print(f"Product name is: {self.name} its price is:{self.price}")

# class discountproduct(product):
#     def display_info(self):
#         super().display_info()
#         print("specal note: 10% discoount applies at checkout ")
        

# p1=discountproduct("laptop",50000)
# p1.display_info()


class camera:
    def __init__(self,brand):
        self.brand=brand

    def capture(self):
        print("Click!! photo saved!! ")


class facedetectedcamera(camera):
    def __init__(self, brand, face_detected):
        self.face_dectected= face_detected
        super().__init__(brand)
        

    def capture(self):
        if self.face_dectected==True:
            super().capture()
        else:
            print("Error: no face detected ")

f1=facedetectedcamera("sony", True)
f1.capture()
    
    