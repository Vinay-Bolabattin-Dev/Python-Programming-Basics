

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
     OOP Polish: Dunder Methods (__str__, __repr__)
=============================================
"""

class ReelExport:
    def __init__(self, topic, fps, size_mb):
        self.topic = topic
        self.fps = fps
        self.size_mb = size_mb

    # 1. Changing the default 'Human View' button
    def __str__(self):
        return f"Reel: {self.topic} ({self.fps} FPS) -> Ready to upload!"

    # 2. Changing the default 'Developer View' button
    def __repr__(self):
        return f"ReelExport(topic='{self.topic}', fps={self.fps}, size_mb={self.size_mb})"


# --- Execution Window ---
# Creating our custom reel object
my_reel = ReelExport("Python Day 11", 60, 45)

# Testing the Dunder methods
print("--- STR OUTPUT (Human View) ---")
print(str(my_reel)) 

print("\n--- REPR OUTPUT (Developer View) ---")
print(repr(my_reel))

