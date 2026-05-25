

"""
=============================================
 Final Expection/Error Handling challeges
=============================================
"""

# video_duration=30
# video_duration=0

# try:
#     render_speed=100/video_duration

# except ZeroDivisionError:
#     print("Error: Duration can not be 0 secounds ")

# else:
#     print("Render successful !! Speed score caculated ")

# finally:
#     print("Closing rendering engine claering temporary cache")


"""
---------------------------------------
raise keyword in exception handling 
--------------------------------------- 
"""

# export_fps = int(input("Enter a export_fps: "))

# try:
#     if export_fps > 60:
#         raise ValueError("CapCut only supports up to 60 Fps for Instagram reels!!")
#     else:
#         print("Fps setting verified !!")

# except ValueError as e :
#     print(e)

# finally :
#     print('Export configuration complete')
     

""" 
===========================================================
   Magic / Dunder Methods:-
===========================================================
"""

"""
=============================================
     OOP Polish: Magic/Dunder Methods (__str__, __repr__)
=============================================
"""
##Easy level example

# class Audio:
#     def __init__(self, track_name , volume):
#         self.track_name=track_name
#         self.volume=volume


#     def __str__(self):
#         return (f"track name is {self.track_name} and volume is {self.volume}")
    

# music =Audio("kirtan", 12)

# print(music)

# class study_topic:
#     def __init__(self, subject_name):
#         self.subject_name= subject_name

#     def show(self):
#         return f"Today's subject to learn is {self.subject_name}"
    
# s1=study_topic("maths")
# s2=study_topic("English")

# topic =[s1, s2]

# print(topic)

## Medium level 

# class Reelpost:
#     def __init__(self, caption, likes_count):
#         self.caption = caption
#         self.likes_count = likes_count

#     def __repr__(self):
#         return (f"Caption:- {self.caption} totaly likes:- {self.likes_count}")
    
# video1=Reelpost("Magic study", 2000)
# video2=Reelpost("Updating python ", 2500)

# post =[video1, video2]

# print(video1)
# print(post)

# class FixedDeposit:
#     def __init__(self, principal ,interest_rate):
#         self.principal =  principal
#         self.interest_rate = interest_rate

#     def __str__(self):
#         return f"Your principal:- {self.principal} & interest rate:- {self.interest_rate}"
    
#     def __repr__(self):
#         return f"Your principal:- {self.principal} & interest rate:- {self.interest_rate}"
    

# c1=FixedDeposit(10000, 3.1)
# print(c1)


## Hard level 

# class Capcutproject:
#     def __init__(self, project_name, video_length_secound , is_exported):
#         self.project_name=project_name
#         self.video_length_secound=video_length_secound
#         self.is_exported = is_exported

#     def __str__(self):
#         if self.is_exported== True:
#             return "Status Ready"
#         else:
#             return "Status: Draft"


#     def __repr__(self):
#         return f"project name :- {self.project_name}\nvideo length:- {self.video_length_secound}\nExport status:- {self.is_exported}"
    
# video1= Capcutproject("IPL", 45 , True)
# video2=Capcutproject("MI", 60 , False)
# print(video1)
# print(video2)

# print(repr(video1)) ## when we want to print __repr__ method without removing __Str__

""" Math magic method"""
##__add__

# class instragram_likes:
#     def __init__(self, count):
#         self.count=count

#     def __add__(self,other):
#         return self.count + other.count
    
#     def __sub__(self, other):
#         return self.count - other.count
    
#     def __mul__(self, other):
#         return self.count * other.count

# reel1=instragram_likes(2000)
# reel2=instragram_likes(10000)
# totallikes= reel1+reel2
# print(totallikes)
# totallikes=reel1-reel2
# print(totallikes)
# totallikes=reel1*reel2
# print(totallikes)

""" __len__ lifecycle / utility magic method"""

class capcutplaylist:
    def __init__(self, video_list):
        self.video_list=video_list

    def __len__(self):
        return len(self.video_list)
    
my_playlist=capcutplaylist("Intro")
print(len(my_playlist))
        