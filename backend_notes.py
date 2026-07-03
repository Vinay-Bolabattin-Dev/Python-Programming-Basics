"""HTTP Methods: Mastering the core actions (GET, POST, PUT, DELETE) """
## Easy level 

import requests

print("--- Day 9: HTTP Methods Initialization ---")

# Step 1: A clean, simple GET request to verify our connection
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print(f"Connection Status: {response.status_code} OK")
print("Environment is ready for tomorrow morning.")