# # # # Movie Theater Pricing

# # # time = float(input("Enter a time(0-24)")) # 1=13 , 2=14, 3=15......

# # # age= int(input('Enter your age: '))

# # # if time<17:
# # #     print("Matinee Price: 100 rs")
# # # else:
# # #     if age <18 :
# # #         print("Evening youth price: 120 rs")
# # #     else:
# # #         print("Evenign Adult price: 150 rs")


# # ## labrary Fine 
# days_late = int(input("How many Days late is the Book??: "))


# if days_late==0:
#     print("No fine, Thank you!! ")
# else:
#     is_student= str (input("Are you student (yes or no ): "))

#     if is_student =="yes":
#         fine= days_late *5
#         print(f"Student Fine: {fine} rs")
#     else:
#         fine=days_late * 10
#         print(f"Standered Fine: {fine} rs")



""" String 
practice + Revision  """

movie_name = "2026_PROJECT_CLIP_01.MP4"


movie_name.strip() # removing extra space 

movie_name[0:5] # printing only year from name 

movie_name.replace("CLIP", "SCENE") # replacing clip to scene 

final_moviename= movie_name.lower()
print(final_moviename)
