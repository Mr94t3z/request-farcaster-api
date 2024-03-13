import requests
import json
import os

def fetch_address_data(user_ids):
    base_url = "https://client.warpcast.com/v2/user"
    address_data = []

    for user_id in user_ids:
        url = f"{base_url}?fid={user_id}"
        response = requests.get(url)

        if response.status_code == 200:
            user_info = response.json()
            if 'result' in user_info and 'extras' in user_info['result']:
                custody_address = user_info['result']['extras'].get('custodyAddress')
                if custody_address is not None:
                    address_data.append(custody_address)
                    print(f"Saved custody address for user ID {user_id}: {custody_address}")
                else:
                    print(f"No custody address found for user ID {user_id}")
            else:
                print(f"User ID {user_id} data not found in the response")
        else:
            print(f"Failed to fetch data for user ID {user_id}. Status code: {response.status_code}")

    return address_data

# Generate list of user IDs from 1 to 1000
user_ids = list(range(1, 1001))

# Fetch custody addresses for the list of user IDs
address_data = fetch_address_data(user_ids)

# Specify the folder where you want to save the file
folder_name = "address_early_1k_farcaster_users"

# Create the folder if it doesn't exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Save fetched custody addresses into a JSON file in the specified folder
file_path = os.path.join(folder_name, "address_data.json")
with open(file_path, "w") as json_file:
    json.dump(address_data, json_file, indent=4)

print(f"Custody addresses saved to {file_path}")
