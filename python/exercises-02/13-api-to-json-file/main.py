# ----------------------------------------
# Project: API To JSON File
#
# Goal:
# - Connect to a real API
# - Receive JSON data
# - Convert API response into Python data
# - Save API data into a JSON file
# ----------------------------------------


# Import libraries

import json
import requests



# ----------------------------------------
# Part 1: API Information
# ----------------------------------------

# GitHub username

username = "TahaRuby"


# Create API URL

url = f"https://api.github.com/users/{username}"



# ----------------------------------------
# Part 2: Send Request To API
# ----------------------------------------

response = requests.get(url)



# ----------------------------------------
# Part 3: Check API Response
# ----------------------------------------

if response.status_code == 200:


    # Convert JSON response into Python dictionary

    user_data = response.json()



    # ----------------------------------------
    # Part 4: Save Data Into JSON File
    # ----------------------------------------

    with open("github_user.json", "w") as file:


        # Convert Python dictionary into JSON file

        json.dump(user_data, file, indent=4)



    print("User data saved successfully!")



else:


    print("Failed to get user data")

    print("Status Code:", response.status_code)