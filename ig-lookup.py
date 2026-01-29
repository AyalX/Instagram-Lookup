import requests

def find_instagram_profile(user_id, session_id):
    url = f"https://i.instagram.com/api/v1/users/{user_id}/info/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Cookie': f'sessionid={session_id}',
        'X-IG-App-ID': '936619743392459'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_info = response.json()
        username = user_info['user']['username']
        return f"https://www.instagram.com/{username}/"
    else:
        return "Unable to retrieve profile."

def find_instagram_id_by_username(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    if response.status_code == 200:
        user_id_start = response.text.find('"profilePage_', 0) + len('"profilePage_')
        user_id_end = response.text.find('"', user_id_start)
        user_id = response.text[user_id_start:user_id_end]
        return user_id
    else:
        return None

def main():
    session_id = input("Enter your Instagram session ID: ")
    choice = input("Enter '1' to search by user ID, or '2' to search by username: ")
    if choice == '1':
        user_id = input("Enter the user ID to search for: ")
        profile_url = find_instagram_profile(user_id, session_id)
        print(profile_url)
    elif choice == '2':
        username = input("Enter the username to search for: ")
        user_id = find_instagram_id_by_username(username)
        if user_id:
            print(f"User ID for {username}: {user_id}")
        else:
            print("Unable to retrieve user ID.")
            
if __name__ == "__main__":
    main()
