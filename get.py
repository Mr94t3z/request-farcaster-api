import requests
import json
import os

def fetch_user_data(user_ids):
    base_url = "https://client.warpcast.com/v2/user"
    user_data = []

    for user_id in user_ids:
        url = f"{base_url}?fid={user_id}"
        response = requests.get(url)

        if response.status_code == 200:
            user_data.append(response.json())
            print(f"Saved account data for fid = {user_id}")
        else:
            print(f"Failed to fetch data for user ID {user_id}. Status code: {response.status_code}")

    return user_data

# Generate list of user IDs from 1 to 1000
user_ids = list(range(1, 1001))

# Fetch user data for the list of user IDs
user_data = fetch_user_data(user_ids)

# Specify the folder where you want to save the file
folder_name = "early_1k_farcaster_users"

# Create the folder if it doesn't exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Save fetched user data into a JSON file in the specified folder
file_path = os.path.join(folder_name, "user_data.json")
with open(file_path, "w") as json_file:
    json.dump(user_data, json_file, indent=4)

print(f"User data saved to {file_path}")
