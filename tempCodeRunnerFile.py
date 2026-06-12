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

truck_load={
    "cement_bags":10,
    "iron_rods":4,
}

new_dilivery={
    "cement_bags" :25,
    "safety_comes": 6,
}

for key, value  in new_dilivery.items():
    if key in truck_load:
        truck_load[key ]=truck_load[key]+value
    else:
        truck_load[key] = value
print(truck_load)

    
