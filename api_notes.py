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
class MockResponse:
    def __init__(self, status_code, data):
        self.status_code=status_code
        self.data=data 

response=MockResponse(404, '{"status": "active", "total_reels":14}')

if response.status_code==200:
    print("print a success message")
elif response.status_code==404:
    print(" Not found Error message ")
else:
    print('unkown server issue')