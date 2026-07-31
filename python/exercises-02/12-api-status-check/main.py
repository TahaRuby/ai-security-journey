# ----------------------------------------
# Project: API Status Check
#
# Goal:
# - Send request to an API
# - Check response status code
# - Handle successful and failed requests
# - Read API data only when request is successful
# ----------------------------------------


# Import requests library
# It allows Python to communicate with APIs

import requests



# ----------------------------------------
# Part 1: API URL
# ----------------------------------------

# GitHub API endpoint
# This API returns information about a GitHub user

url = "https://api.github.com/users/github"



# ----------------------------------------
# Part 2: Send API Request
# ----------------------------------------

# Send GET request to the API

response = requests.get(url)



# ----------------------------------------
# Part 3: Check Status Code
# ----------------------------------------

# Status code tells us if the request was successful or not
#
# 200 -> Success
# 404 -> Not Found
# 500 -> Server Error

print("Status Code:", response.status_code)



# ----------------------------------------
# Part 4: Handle Successful Response
# ----------------------------------------

# If the request is successful,
# convert JSON response into Python dictionary

if response.status_code == 200:

    data = response.json()


    print("----------------")
    print("Request Successful")


    # Display selected information

    print("Username:", data["login"])
    print("Followers:", data["followers"])
    print("Public Repositories:", data["public_repos"])



# ----------------------------------------
# Part 5: Handle Errors
# ----------------------------------------

else:

    print("----------------")
    print("Request Failed")
    print("Error Code:", response.status_code)