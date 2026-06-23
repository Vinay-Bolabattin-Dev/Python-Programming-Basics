# # Step 1: The Simulation Blueprint
# class MockResponse:
#     def __init__(self, status_code, data_string):
#         self.status_code = status_code
#         self.data = data_string

# # Step 2: Create a simulated successful connection (200 OK)
# response = MockResponse(200, '{"status": "active", "total_reels": 14}')

# # Step 3: The inspection logic
# if response.status_code == 200:
#     print("Success: Connected to server safely.")
#     print(f"Payload Received: {response.data}")
# elif response.status_code == 404:
#     print("Error: Resource not found (404). Check your destination URL.")
# else:
#     print(f"Error: Unknown server issue. Status code: {response.status_code}")

""" Easy level test """
# class MockResponse:
#     def __init__(self, status_code, data):
#         self.status_code=status_code
#         self.data=data 

# response=MockResponse(404, '{"status": "active", "total_reels":14}')

# if response.status_code==200:
#     print("print a success message")
# elif response.status_code==404:
#     print(" Not found Error message ")
# else:
#     print('unkown server issue')

""" Easy level test """
# class MockResponse:
#     def __init__(self, status_code, data):
#         self.status_code=status_code
#         self.data=data 

# def secure_api_request(url , token ):
#     if url=="http://api.securedata.com" and token == "securet_token_123":
#         return MockResponse(200,'{"access": "granted"}')
#     elif url=="http://api.securedata.com" and token !="securet_token_123":
#         return MockResponse(401,'{"error": "Invalid Token"}')
#     else:
#         return MockResponse(404, "")
        
# result = secure_api_request("http://api.securedata.com", "securet_token_1234")  


# if result.status_code == 200:
#     print(f"Success: {result.data}")
# elif result.status_code == 401:
#     print("Access Denied: Bad Credentials")
# elif result.status_code == 404:
#     print("Not Found") 


""" Medium level test"""
# class MockResponse:
#     def __init__(self, status_code, data):
#         self.status_code=status_code
#         self.data=data 

# def upload_video_api(file_size_mb):
#     if file_size_mb <=0:
#         return MockResponse(404,'{"error": "Invalid file size"}')
#     elif file_size_mb>500:
#         return MockResponse(413,'{"error": "file exceeds 500MB limit"}')
#     else:
#         return MockResponse(200, '{"status": "uploaded", "processing": True }')
        

# upload_result=upload_video_api(600)

# if upload_result.status_code==200:
#     print(f"Success: {upload_result.data}")
# elif upload_result.status_code==400:
#     print(f"Error :{upload_result.data}")
# elif upload_result.status_code==413:
#     print(f"playload {upload_result.data}")
# else:
#     print("Not Found ")



""" Hard level test"""
# class MockResponse:

    
#     def __init__(self, status_code, data):
#         self.status_code=status_code
#         self.data=data 

# def get_user_profile(username):
#     database={"vinay": '{"role": "engineer", "status": "active"}' , "guest":'{"role": "viewer", "status": "restricted"}' }
#     if username in database:
#         return MockResponse(200,database[username])
#     else:
#         return MockResponse(404, '{Error: "user not found "}')

# profile_Call =get_user_profile("vinay")

# if profile_Call.status_code==200:
#     print(f"successful!!: {profile_Call.data}")
# elif profile_Call.status_code==404:
#     print(f"Error: User is not avilable")



# class OrderRecepit:
#     def __init__(self,status_code, payload):
#         self.status_code=status_code
#         self.payload=payload

# def process_order(item_id,quantity):
#     stock_room={"phone": 5 , "laptop":2}

#     if item_id not in stock_room:
#         return OrderRecepit(404,'{error: "Item out of stock or does not exist!!" }')
#     elif item_id in stock_room and quantity>stock_room[item_id]:
#         return OrderRecepit(400,'{"error": "Insufficient stock avaliable"}')
#     else:
#         return OrderRecepit(200,'{"status": "Order approved", " shippling": true}')
    
# order_call= process_order("phone", 10)

# if order_call.status_code==200:
#     print(f"successfully Ordered: {process_order.payload}")
# elif order_call.status_code==404:
#     print(f'unsuccessful order: {process_order.payload}')
# else:
#     print(f" Sorry!! Insufficinet stock")