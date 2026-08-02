# ----------------------------------------
# Project: Class Wraps API
#
# Goal:
# - Use OOP with API requests
# - Create a class for API operations
# - Store username inside object
# - Fetch GitHub user data
# - Handle API response status
# ----------------------------------------


# Import libraries

import requests



# ----------------------------------------
# Part 1: Create GithubUser Class
# ----------------------------------------

class GithubUser:


    # Constructor
    # Receives username and stores it

    def __init__(self, username):

        self.username = username



    # Method to fetch user data from GitHub API

    def fetch(self):


        # Create API URL using username

        url = f"https://api.github.com/users/{self.username}"


        # Send GET request to API

        response = requests.get(url)



        # Check if request was successful

        if response.status_code == 200:


            # Convert JSON response into Python dictionary

            return response.json()


        else:


            # Return None if user does not exist

            return None





# ----------------------------------------
# Part 2: Create Object
# ----------------------------------------

user = GithubUser("TahaRuby")



# ----------------------------------------
# Part 3: Fetch User Data
# ----------------------------------------

result = user.fetch()



# ----------------------------------------
# Part 4: Display Result
# ----------------------------------------

if result:


    print("Username:", result["login"])

    print("Followers:", result["followers"])

    print("Public Repositories:", result["public_repos"])


else:

    print("User not found")