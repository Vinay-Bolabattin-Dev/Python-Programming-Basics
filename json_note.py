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

user_profile = {
    "user_id": 707,
    "settings": {
        "dark_mode": True,
        "notifications": False
    }
}

serialization_profile_string= json.dumps(user_profile)

print(type(serialization_profile_string))

print(f"Serialized Profile:{serialization_profile_string}")