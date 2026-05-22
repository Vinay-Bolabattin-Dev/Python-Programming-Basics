

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

export_fps = int(input("Enter a export_fps: "))

try:
    if export_fps > 60:
        raise ValueError("CapCut only supports up to 60 Fps for Instagram reels!!")
    else:
        print("Fps setting verified !!")

except ValueError as e :
    print(e)

finally :
    print('Export configuration complete')
     
