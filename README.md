# Instagram Profile Search

This script allows you to search for an Instagram profile using either the user ID or the username. It utilizes the Instagram API to retrieve profile information based on the provided input.

## Prerequisites
- Python 3.x
- Requests library (`pip install requests`)

## Session ID
In order to use this script, you need to provide your Instagram session ID. The session ID is a unique identifier associated with your Instagram login session, and it is required to authenticate your requests to the Instagram API.

To obtain your Instagram session ID, you can follow these steps:

1. Open Instagram in your web browser.
2. Log in to your Instagram account.
3. Right-click on the page and select "Inspect" to open the browser's developer tools.
4. In the developer tools, navigate to the "Application" tab.
5. In the left sidebar, expand the "Cookies" section and select "https://www.instagram.com".
6. Look for a cookie named "sessionid" and copy its value.

![Session ID](session_id.png)

## Usage
1. Clone the repository or download the script.
2. Install the required dependencies by running `pip install requests` in your terminal.
3. Open the script in a text editor.
4. Replace the placeholder `SESSION_ID` with your Instagram session ID.
5. Save the changes to the script.
6. Run the script by executing `python script.py` in your terminal.

You will be prompted to choose the search method: either by user ID or by username. Provide the required information and follow the instructions to retrieve the desired Instagram profile.

Please note that hardcoding the session ID in the script is not secure, and the session ID will eventually expire. In a production environment, you would typically want to use OAuth to obtain a temporary access token for authentication.

## License
This project is licensed under the [MIT License](LICENSE).
