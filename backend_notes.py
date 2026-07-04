"""HTTP Methods: Mastering the core actions (GET, POST, PUT, DELETE) """
## Easy level & medium level example together !! 

import requests
import json 


# url_get=("https://jsonplaceholder.typicode.com/posts/5")
# ##Get request
# response_get=requests.get(url_get)

# print(f"Get Titile : {response_get.json()["title"]}")
# ##POST request

# url_post=("https://jsonplaceholder.typicode.com/posts/")

# new_data= {
#     "title": "Day 9 Code", 
#     "body": "Writing backend logic",
#     "userId": 21, 
#     "id": 10,
# }

# response_post=requests.post(url_post, json=new_data)
# print(f"POST data Title: {response_post.json()["title"]}")


# url_put=("https://jsonplaceholder.typicode.com/posts/1")

# updated_data={
#     "id": 1,
#     "title": "Updated Title",
#     "body": "Updated Body", 
#     "userId": 21
# }

# response_put=requests.put(url_put,json=updated_data)
# print(f"updated data: {response_put.json()["title"]} ")
# print(response_put.status_code)


# url_delete=("https://jsonplaceholder.typicode.com/posts/1")
# response_delete=requests.delete(url_delete,json=updated_data)
# print(response_delete.status_code)
# print(response_put.status_code)


""" another example of HTTP methods to solve & test """

# link_Get=("https://jsonplaceholder.typicode.com/todos/7")
# Response_2nd_get=requests.get(link_Get)
# print(f"Get title: {Response_2nd_get.json()["title"]}")


# link_Post=("https://jsonplaceholder.typicode.com/todos/")
# new_data_on_link={
#     "title": "Master Backend Development", 
#     "completed": False, 
#     "userId": 21}

# Response_2nd_post=requests.post(link_Post, json=new_data_on_link)
# print(f"checking stastus_code: {Response_2nd_post.status_code}")


# link_put=("https://jsonplaceholder.typicode.com/todos/7")

# updating_link_data={
#     "id": 7, 
#     "title": "Updated Todo Title",
#     "completed": True, 
#     "userId": 21}
# Response_2nd_Put=requests.put(link_put, json=updating_link_data)
# print(Response_2nd_Put.status_code)


# links_delete=("https://jsonplaceholder.typicode.com/todos/7")
# Response_2nd_delete=requests.delete(links_delete)
# print(Response_2nd_delete.status_code)


""""HTTP Status Codes: Decoding responses (200 OK, 201 Created, 404 Not Found, 500 Server Error)"""

# --- Milestone 4: HTTP Status Codes numbers short notes---
# 2xx = Success (200 = OK [GET, PUT, DELETE], 201 = Created[POST])
# 4xx = Client Error (400 = Bad Request, 401 = No Auth, 404 = Not Found)
# 5xx = Server Error (500 = Backend Crash)


""" Level wise example """

url= ("https://jsonplaceholder.typicode.com/posts/999999")

response=requests.get(url)
if response.status_code==200:
    print(f"{response.status_code}: Success!! Data Found")
elif response.status_code==404:
    print(f"{response.status_code}: Error: Post does not exist")
else:
    print(f"{response.status_code}: Something else went wrong!! ")


url_post=("https://jsonplaceholder.typicode.com/posts/")
new_data={
    "title": "Final Milestone Check", 
    "body": "Testing status logic", 
    "userId": 21
}


post_reponse=requests.post(url_post, json=new_data)
if post_reponse.status_code==201:
    print(f"{post_reponse.status_code}: Resourcce successfully Created")
else:
    print(f"Failed to create resource. Status code:{post_reponse.status_code}")
