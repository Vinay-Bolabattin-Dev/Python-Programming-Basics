import json 
"""  Easy level : Deserialization (json.loads())"""
# api_string= '{"reel_id":9081, "is_published": true, "sponser": null }'
# print(type(api_string))

# reel_dict=json.loads(api_string)
# print(reel_dict)
# print(type(reel_dict))

# status=reel_dict.get("is_published")
# print(f"publisher statues : {status}")
""" Easy Level : Serialization (json.dumnps )"""
# profile_dict={
#     "username":"editor_pro",
#     "verified":False,
#     "clips_count":14,
# }

# json_output_string=json.dumps(profile_dict)

# print(type(json_output_string))
# print(f"Serialization JSON String: {json_output_string}")

"""  Medium level : Deserialization (json.loads())"""

# nested_api_string='{"project_id": 404, "details": {"category": "reels", "is_approved": true}}'

# project_dict= json.loads(nested_api_string)
# print(project_dict)

# project_category= project_dict.get("details").get("category")
# print(f"Project category: {project_category}")
""" medium Level : Serialization (json.dumnps )"""

# user_profile = {
#     "user_id": 707,
#     "settings": {
#         "dark_mode": True,
#         "notifications": False
#     }
# }

# serialization_profile_string= json.dumps(user_profile)

# print(type(serialization_profile_string))

# print(f"Serialized Profile:{serialization_profile_string}")


"""  Hard level : Deserialization (json.loads())"""

# complex_api_string='{"campaign":"Summmer Sale ", "reel_list":[{"id":1,  "view":150}, {"id":2, "view":300}]}'

# campaign_dict= json.loads(complex_api_string)

# total_view= 0

# reels=campaign_dict.get("reel_list", [])
# for reel_item in reels:
#     total_view += reel_item.get("view", 0)

# print(f"total compaign views: {total_view}")


# storage_api_string= '{ "user": "editor_pro","project_file":[{"name":"reel_01.mp4", "size_mb":45}, {"name":"intro.mp4","size_mb":15} , {"name":"draft.mp4", "size_mb":110}]}'

# stroage_dict=json.loads(storage_api_string)

# total_size=0

# size=stroage_dict.get("project_file", [])
# for mb in size :
#     total_size += mb.get("size_mb", 0)

# print(f"total size of file is: {total_size}")

""" Hard Level : Serialization (json.dumnps )"""

# analytics_data = {
#     "platform": "Instagram",
#     "metrics": [
#         {"type": "reel", "count": 12},
#         {"type": "story", "count": 25}
#     ]
# }
# pretty_json_string=json.dumps(analytics_data, indent= 4)
# print(pretty_json_string)

""" milestone 4 :  json File I/O json.load(), json.dump()"""


""" Easy level Write and read operation """
# export_data = {
#     "format": "Mp4",
#     "fps": 60,
#     "render": True
# }

# with open("reel_config.json", 'w') as file:
#     json_file=json.dump(export_data,file)

# with open("reel_config.json", "r") as file:
#     impoerted_dict=json.load(file)
#     print(f" Loaded Dicitnary Data: {impoerted_dict}")

""" Medium level Write and read operation """


# project_data = {
#     "project_name": "Reel_V1",
#     "settings": {
#         "resolution": "1080x1920",
#         "audio_boost": True
#     }
# }

# with open("formatted_project.json", "w") as file:
#     A=json.dump(project_data, file, indent=4)

# with open("formatted_project.json", "r") as file:
#     loaded_project=json.load(file)

# video_res= loaded_project.get("settings").get("resolution")
# print(f"Target Resolution: { video_res}")

""" Hard level Write and read operation """

raw_batch = {"batch_id": 101, "clips": [{"id": "A", "duration": 15}, {"id": "B", "duration": 30}]}

with open("input_batch.json", "w") as file:
    json.dump(raw_batch, file)

with open("input_batch.json", "r") as infile:
    batch_dict=json.load(infile)

total_duration=0
clip_list=batch_dict.get("clips", [])

for clip in clip_list:
   total_duration += clip.get("duration", 0)

batch_dict["total_routine"] = total_duration

with open ("processed_batch.json", "w") as outfile:
    json.dump(batch_dict,outfile,indent=4)