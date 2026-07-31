# ----------------------------------------
# Project: First API Call
#
# Goal:
# - Send request to an API
# - Receive response
# - Convert JSON response to Python data
# ----------------------------------------


# Import requests library
import requests



# API URL
url = "https://api.github.com/users/github"



# Send GET request
response = requests.get(url)



# Convert response JSON into Python dictionary
data = response.json()



# Display data

print(data)


print("----------------")


print("Username:", data["login"])
print("Followers:", data["followers"])
print("Public Repositories:", data["public_repos"])