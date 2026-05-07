# # # # # # # # # # # # # Movie Theater Pricing

# # # # # # # # # # # # time = float(input("Enter a time(0-24)")) # 1=13 , 2=14, 3=15......

# # # # # # # # # # # # age= int(input('Enter your age: '))

# # # # # # # # # # # # if time<17:
# # # # # # # # # # # #     print("Matinee Price: 100 rs")
# # # # # # # # # # # # else:
# # # # # # # # # # # #     if age <18 :
# # # # # # # # # # # #         print("Evening youth price: 120 rs")
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         print("Evenign Adult price: 150 rs")


# # # # # # # # # # # ## labrary Fine 
# # # # # # # # # # days_late = int(input("How many Days late is the Book??: "))


# # # # # # # # # # if days_late==0:
# # # # # # # # # #     print("No fine, Thank you!! ")
# # # # # # # # # # else:
# # # # # # # # # #     is_student= str (input("Are you student (yes or no ): "))

# # # # # # # # # #     if is_student =="yes":
# # # # # # # # # #         fine= days_late *5
# # # # # # # # # #         print(f"Student Fine: {fine} rs")
# # # # # # # # # #     else:
# # # # # # # # # #         fine=days_late * 10
# # # # # # # # # #         print(f"Standered Fine: {fine} rs")



# # # # # # # # # # """ String 
# # # # # # # # # # practice + Revision  """

# # # # # # # # # # movie_name = "2026_PROJECT_CLIP_01.MP4"


# # # # # # # # # # movie_name.strip() # removing extra space 

# # # # # # # # # # movie_name[0:5] # printing only year from name 

# # # # # # # # # # movie_name.replace("CLIP", "SCENE") # replacing clip to scene 

# # # # # # # # # # final_moviename= movie_name.lower()
# # # # # # # # # # print(final_moviename)


# # # # # # # # # # ## List 
# # # # # # # # # # assets = ["intro", "vlog_clip", "outro"]


# # # # # # # # # # assets[1 ]= "cinematic_shot"

# # # # # # # # # # assets.append("Background_music")

# # # # # # # # # # assets.sort()
# # # # # # # # # # print(assets)

# # # # # # # # # # ## slicing in list 
# # # # # # # # # # a= assets[0:2]
# # # # # # # # # # print(a)

# # # # # # # # # ## TUPLES
# # # # # # # # # #Example 1
# # # # # # # # # # required_resolution=(1970, 1080)
# # # # # # # # # # width=int(input('Enter a width: '))
# # # # # # # # # # height= int (input("Enter a height: "))

# # # # # # # # # # if width == required_resolution[0] and required_resolution[1]:
# # # # # # # # # #     print("Resolution Match! Ready to export")

# # # # # # # # # # else:
# # # # # # # # # #     print("Warning: Resolution mismatch.")

# # # # # # # # # #example 2:

# # # # # # # # # # peack_hours=(10,14, 20) #(representing 10 AM, 2 PM, and 8 PM).

# # # # # # # # # # post_time= int(input("Enter you post time: "))

# # # # # # # # # # if post_time == peack_hours[0] or post_time== peack_hours[2]:
# # # # # # # # # #     print("Excellent timing! High engagement expected")
# # # # # # # # # # else:
# # # # # # # # # #     print("standard post time ")


# # # # # # # # # # """ Dictionary """

# # # # # # # # # # #creating a Dictionary 

# # # # # # # # # # mi_player ={
# # # # # # # # # #     "name":"Rohit sharma",
# # # # # # # # # #     "team":"Mumbai Indians",
# # # # # # # # # #     "runs": 105 ,
# # # # # # # # # #     "lat_five_score": [105,10,36,0,11],
    
# # # # # # # # # #     "squad":{ 
# # # # # # # # # #         "player_name": ["Rohit", "ishan", "Hardik", "Surya"]
    

# # # # # # # # # #     },
# # # # # # # # # #     "unique_team":{"MI",'MI', "CSK"}

    

# # # # # # # # # # }

# # # # # # # # # # # print(mi_player["lat_five_score"][-1])
# # # # # # # # # # # print(mi_player.keys())
# # # # # # # # # # # print(mi_player.get("team"))
# # # # # # # # # # print(mi_player["squad"]["player_name"])  
# # # # # # # # # # mi_player["squad"]["player_name"].append("Bumarah")
# # # # # # # # # # # print(mi_player["squad"].values())
# # # # # # # # # # mi_player["squad"]["player_name"].append("Rohit")
# # # # # # # # # # print(mi_player["squad"]["player_name"])
# # # # # # # # # # print(mi_player.get("unique_team"))

# # # # # # # # # ## SET 

# # # # # # # # # mi_squad ={"Rohit", "Bumrah", " Hardik", "Sky"}

# # # # # # # # # indian_squad={"Gill", "Sanju", "Rohit", "Bumrah", 'Virat', "Sky"}

# # # # # # # # # print(mi_squad.union(indian_squad))

# # # # # # # # # mi_squad.add("Tilak")
# # # # # # # # # print(mi_squad)
# # # # # # # # # print(mi_squad.intersection(indian_squad))
# # # # # # # # # indian_squad.clear()
# # # # # # # # # print(indian_squad)


# # # # # # # # ## Loops  

# # # # # # # # # count =1
# # # # # # # # # total_sum =0
# # # # # # # # # while count <=5:
# # # # # # # # #     total_sum+=count
# # # # # # # # #     count +=1
# # # # # # # # # print(total_sum)

# # # # # # # # num=1
# # # # # # # # factorial=1
# # # # # # # # while num<=5:
# # # # # # # #     factorial=factorial*num
# # # # # # # #     num+=1
# # # # # # # # print(factorial)

# # # # # # # # num=1
# # # # # # # # while num <=15:
# # # # # # # #     if num %2!=0:
# # # # # # # #         print(num)
# # # # # # # #     num +=1

# # # # # # # # ## Divided by 3
# # # # # # # # number =1
# # # # # # # # while number <=20:
# # # # # # # #     if number % 3 ==0:
# # # # # # # #         print(number)
# # # # # # # #     number+=1

# # # # # # # # ##print 1 to 10 but skip 7 
# # # # # # # # n=0
# # # # # # # # while n <=10:
# # # # # # # #     n +=1
# # # # # # # #     if n==7:
# # # # # # # #         continue
# # # # # # # #     print(n)


# # # # # # # # ##string loop
# # # # # # # # code =""
# # # # # # # # while code !="MI": 
# # # # # # # #     code= str (input ("Enter a vaild code for access: "))
# # # # # # # #     if code == "MI":
# # # # # # # #         print("Access Granted! Go ahead!")
# # # # # # # #     else:
# # # # # # # #         print("Not valid code")
    
# # # # # # # # count=1
# # # # # # # # while count<=20:
# # # # # # # #     if count %5==0:
# # # # # # # #         print(count)
# # # # # # # #     count +=1

# # # # # # # ##list loops
# # # # # # # players = ["Rohit", "Surya", 'Tilak' , "Hardik", "Bumrah"]
# # # # # # # index=0
# # # # # # # while index < (len(players)):
# # # # # # #     if players[index] =="Hardik":
# # # # # # #         break
# # # # # # #     print(players[index])
# # # # # # #     index +=1

# # # # # # ##hard question 
# # # # # # # index=0
# # # # # # # total_score=0

# # # # # # # while index < len(runs):
# # # # # # #     if runs[index] ==0:
# # # # # # #         index +=1
# # # # # # #         continue
# # # # # # #     total_score+=runs[index]
# # # # # # #     index +=1

# # # # # # # print(f"total sore: {total_score}")

# # # # # # ##advanced question 
# # # # # # # match_scores = [15, 48, 22, 96, 10, 35]
# # # # # # # index = 0
# # # # # # # big_hits = 0
# # # # # # # small_scores = 0

# # # # # # # while index < len(match_scores):
# # # # # # #     if match_scores[index]>=30:
# # # # # # #         big_hits +=1
# # # # # # #     else:
# # # # # # #         small_scores +=1
# # # # # # #     index +=1
# # # # # # # print(f"total number of big hits {big_hits} & small scores {small_scores}")

# # # # # # # prices = [120, 450, 0, 890, 300]
# # # # # # # index = 0

# # # # # # # while index < len(prices):
# # # # # # #     if prices[index]==0:
# # # # # # #         prices[index]=500
# # # # # # #         print(f"Fount the error at the {index}, updated it with {prices[index]}")
# # # # # # #         break
    
# # # # # # #     index +=1
# # # # # # # print(prices)
    
# # # # # # """ FOR  
# # # # # #    LOOPS 
# # # # # # Question practice / revision  """
# # # # # # # Ex:1 
# # # # # # # number=[1,2,3,4,5]

# # # # # # # for num in number:
# # # # # # #     print(num*10)

# # # # # # # # Ex:2
# # # # # # # scores = [25, 60, 45, 90, 30, 100]
# # # # # # # for n in scores:
# # # # # # #     if n>=50:
# # # # # # #         print(n)

# # # # # # #Ex:3
# # # # # # runs = [40, 10, 50, 0, 20]
# # # # # # total = 0
# # # # # # for i in runs:
# # # # # #     total+=i
# # # # # # print(total)

# # # # # ## Range()
# # # # # # for i in range(1,11):
# # # # # #     print(i)


# # # # # # for table in range(1,11):
# # # # # #     print(f"5*{table}")
# # # # # # or 
# # # # # # for table in range(5,55,5):
# # # # # #     print(table)

# # # # # # players = ["Rohit", "Surya", "Tilak", "Hardik"]

# # # # # # for i in range (len(players)):
# # # # # #     print(f"Rank {i}:{players[i]}")

# # # # # ## Print only the players who are at an even rank or index using [range(),for loop and if logic]
# # # # # # players = ["Rohit", "Surya", "Tilak", "Hardik", "Bumrah"]

# # # # # # for i in range ((len(players))):
# # # # # #     if i %2==0:
# # # # # #         print(players[i])

# # # # # ## Print only the players who are at an even rank or index using range()
# # # # # players = ["Rohit", "Surya", "Tilak", "Hardik", "Bumrah"]
# # # # # for i in range(0,len(players),2):
# # # # #     print(i,players[i])

# # # # ## Nested Loops 
# # # # for i in range (1,3):
# # # #     for j in range (1,4):
# # # #         print(f"Row {i} , Column {j}")


# # # for i in range(1,4):
# # #     for j in range (1,4):
# # #         print("*" ,end=" ")
# # #     print() # to move next line 

# # # rows=["A", "B"]
# # # for r in rows:
# # #     print(f"Row {r}:", end=" ")
# # #     for s in range(1,4):
# # #         print(s, end=" ")
# # #     print()

# # # all_teams = [
# # #     [10, 20, 30], # Team 1
# # #     [40, 50, 60]  # Team 2
# # # ]
# # # for team in all_teams:
# # #     for score in team:
# # #         print(score)

# # ###Pattern  printing by using loops 
# # # for i in range(1,6):
# # #     print(end=" ")
# # #     for j in range(i):
# # #         print("*", end="")
# # #     print()

# # # size = int(input("Enter a Traingel size to print: "))
# # # for i in range(1,size+1):
# # #     for j in range (i):
# # #         print("*", end="")
# # #     print()

# # # size = int(input("Enter a Traingel size to print: "))
# # # for i in range(size, 0 , -1):
# # #     for j in range (i):
# # #         print("*", end="")
# # #     print()

# # size = int(input("Enter a Traingel size to print: "))

# # for i in range(1,size+1):
# #     for j in range (i):
# #         print("#", end="")
# #     print()

# # for i in range(size-1,0,-1):
# #     for j in range(i):
# #         print("#", end="")
# #     print()


# # size= int (input("Enter a size: "))
# # symbol= input("Enter a symbol:")

# # for i in range(1,size+1):
# #     for j in range(i):
# #         print(f"{symbol}", end="")
# #     print()

# size= int (input("Enter a size: "))
# symbol= input("Enter a symbol:")

# for i in range(1,size+1):
#     for j in range(i):
#         print(f"{symbol}", end="")
#     print()
# for i in range(size-1,0, -1):
#     for j in range(i):
#         print(f"{symbol}", end="")
#     print()


## Pass statemnt :
"""" pass statement is a null statement that does nothing,
just used to work placeholder for future code 
Ex: """
def game_over():
    #I'll finish tomorrow!
    pass
