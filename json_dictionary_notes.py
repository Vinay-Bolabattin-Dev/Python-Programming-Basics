# site_crew={
#     "role": 2520,
#     "names": "mahesh"
# }
# print(site_crew)
# print(f'name of worker is : {site_crew["names"]}')
# print(f'role number  of worker is : {site_crew["role"]}')
# site_crew["role"]=2000
# print(site_crew)

# site_tools={
#     "driller": 912039448439,
#     "Engineer": 7505963833,
#     "Ciment": 2305983934
# }
# print(site_tools)
# site_tools["worker"]=24908909482
# print(site_tools)
# site_tools.update(driller=9120394484)
# print(site_tools)   


# inventory={
#     "ciment_bags":15,
#     "bricks": 500

# }
# print(inventory)
# if inventory.get("supervison"):
#     print(True)
# else:
#     print(False)
#     inventory["supervison"]="Rajgopal"

# print(inventory)
# inventory["bricks"]+=200
# print(inventory)

# truck_load={
#     "cement_bags":10,
#     "iron_rods":4,
# }

# new_dilivery={
#     "cement_bags" :25,
#     "safety_comes": 6,
# }

# for key, value  in new_dilivery.items():
#     if key in truck_load:
#         truck_load[key]=truck_load[key]+value
#     else:
#         truck_load[key] = value
# print(truck_load)

  
""" 
========================================
 del keyword & .pop() metohd
========================================="""

# scarp_yard={
#     "broken_chair": 1,
#     "old_newspaper":5,
#     "damaged_cable":3,
# }
# print(scarp_yard)
# del scarp_yard["broken_chair"]
# print(scarp_yard)
# recycled_paper=scarp_yard.pop("old_newspaper")
# print(recycled_paper)
# print(scarp_yard)

# site_manifest={
#     "surplus_bricks": 120,
#     "broken_tiles":45 ,
# }

# status= site_manifest.pop("missing_pallets", "iteam not found in database") 
# print(site_manifest)
# print(status)

# site_waste={
#     "cocrete_rubble":500,
#     "plastic_warps":5,
#     "broken_timber":250,
#     "paper_cups": 2,
# }
# iteam_to_remove=[]

# for s in site_waste:
#     if site_waste[s]<=10:
#         iteam_to_remove.append(s)

# for a in iteam_to_remove:
#         site_waste.pop(a)
# print(site_waste)

"""" .get() method """
        
# site_equipment={
#     "excavator": 1,
#     "drilling_machine": 2,
    
# }    
# safe_look= site_equipment.get("concerte_mixer")# after writing it so it doesn't crash your script!
# print(safe_look)

# custom_look=site_equipment.get("concerte_mixer", 0)
# print(custom_look)

# project_requirements={
#     "excavator":2,
#     "dump_truck":5,
#     "crane":0,

# }
# qty=project_requirements.get("bulldozer", 0)
# print(qty)
# if qty>0:
#     print("Equiment is available on site")
# else:
#     print("Order required immediately!! ")

""""
=============================================
 `.keys()`, `.values()`, and `.items()`
---------------------------------------------
 """

# row_materials={
#     "cement":150,
#     "steel_bars":80,
#     "sand":300,

# }
# all_keys=row_materials.keys()
# print(all_keys)

# all_values=row_materials.values()
# print(all_values)

# all_pairs=row_materials.items()
# print(all_pairs)

# clean_keys_list=list(row_materials.keys())
# print(clean_keys_list)

# if "timber" in clean_keys_list:
#     print("timber is registered ")
# else:
#     print("timber is missing from inventory lists")

""" Iteration Flow using .items() and for loops  """

# labor_force={
#     "masons":12,
#     "carpenters": 4,
#     "helpers":25,

# }
# total_workers=0
# for role, coumt in labor_force.items():
#     print(f"Role: {role} | Workers:{coumt}")
#     if coumt >5:
#         print(f"large crew required for {role}:{coumt} workers")


# for role, count in labor_force.items():
#     total_workers +=count
# print(f"Total workforce deployment: {total_workers}")

""" Data Hierachies  (Nested objects)"""

# site_details = {
#     "project_A": {
#         "location": "Sector 5",
#         "budget": 50000
#     }
# }

# project_budget= site_details["project_A"]['budget']
# print(project_budget)

# safe_budget= site_details.get("project_B", {}).get("budget", 0)
# print(safe_budget)

# company_branches = {
#     "North_Branch": {"active_projects": 3},
#     "South_Branch": {"active_projects": 5},
#     "East_Branch": {}  # Notice this branch has no active_projects key inside it!
# }


# total_active_projects=0

# for branch , data in company_branches.items():
#     count=data.get("active_projects", 0)
#     total_active_projects += count
#     print(count)

# print(f"Total company active projects: {total_active_projects}")

server_farm={
    "server_Alpha": {"sessions": 140},
    "sever_Beta":{"sessions": 210},
    "server_Game":{} 
}

total_sessions=0
for server , session in server_farm.items():
    session_count=session.get("sessions", 0)
    total_sessions += session_count
    print(session_count)

print(f"total network traffic : {total_sessions} active users")