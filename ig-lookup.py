import requests
from pyfiglet import Figlet
from termcolor import colored
from argparse import ArgumentParser, Namespace


def print_hi(header):
    f = Figlet(font="standard", width=180)
    welcome = colored(f.renderText(text=header), "yellow")
    if readargs().verbose is not False:
        print(f"\n{welcome}")
    pass


def printincolor(word, color='white'):
    print(colored(word, color))
    pass


def readargs() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("-s", "--session", dest="session", help="your own session, you will find it in inspect element", required=True)
    parser.add_argument("-u", "--username", dest="username", help="Enter the username to lookup", required=False)
    parser.add_argument("-i", "--userid", dest="userID", help="Enter the userID to lookup", required=False)
    parser.add_argument("-q", "--quiet", action="store_false", dest="verbose", default=True, help="don't print status messages to stdout", required=False)
    arguments = parser.parse_args()
    # ArgumentParser
    return arguments
    pass


def find_instagram_profile(user_id, session_id):
    url = f"https://i.instagram.com/api/v1/users/{user_id}/info/"
    headers = {
        'User-Agent': 'Instagram 10.3.2 (iPhone7,2; iPhone OS 9_3_3; en_US; en-US; scale=2.00; 750x1334) AppleWebKit/420+',
        'Cookie': f'sessionid={session_id}'
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
    # session_id = input("Enter your Instagram session ID: ")
    print_hi("Instagram-lookup")
    args = readargs()
    # choice = input("[*] Enter '1' to search by user ID, or '2' to search by username: ")
    if args.userID is not None:
        # user_id = input("[*] Enter the user ID to search for: ")
        profile_url = find_instagram_profile(args.userID, args.session)
        printincolor(f"[+] userID {args.userID} refers to: {profile_url}", "blue")
    elif args.username is not None:
        # username = input("[*] Enter the username to search for: ")
        user_id = find_instagram_id_by_username(args.username)
        if user_id:
            printincolor(f"[+] User ID for {args.username}: {user_id}", "green")
        else:
            printincolor("[-] Unable to retrieve user ID.", "red")
    else:
        printincolor("[-] username or userID one should be in use", "red")

    printincolor("[*] DONE\n", "blue")


if __name__ == "__main__":
    main()
    printincolor("AyalX", "yellow")
