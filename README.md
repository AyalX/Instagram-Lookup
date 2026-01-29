# Instagram Profile Search and ID Lookup

A lightweight, minimal Python script to perform reverse lookups on Instagram. This tool allows you to convert a Username to a User ID or retrieve a profile URL from a User ID using direct API requests.

## Project Goal

This project was built with a specific goal: **absolute simplicity**.

Unlike complex scraping frameworks or heavy libraries that require extensive setup, this script provides a raw, transparent implementation. It is designed to be easily understood and used. It does exactly one task - resolving user entities with minimal overhead.

## Capabilities

* **User ID Lookup:** Convert any Instagram username into its unique numeric User ID.
* **Profile Discovery:** Locate a specific Instagram profile URL using only a numeric User ID.
* **Account Tracking:** While usernames and profile pictures can be changed, the User ID remains permanent. This allows you to locate and identify a specific user even after they have completely renamed their account.
* **OSINT Friendly:** Useful for Open Source Intelligence gathering and data analysis.
* **Minimal Dependencies and Risk:** Runs purely on Python and the standard `requests` library.

## Prerequisites

* Python 3.x
* Requests library

```bash
pip install requests

```

## Session ID Configuration

To authenticate requests and avoid immediate login walls, this script requires a valid Instagram Session ID. This is a browser cookie that validates your identity.

**How to retrieve your Session ID:**

1. Open Instagram.com in your web browser.
2. Log in to your account.
3. Right-click anywhere on the page and select **Inspect** to open Developer Tools.
4. Navigate to the **Application** tab (Chrome/Edge) or **Storage** tab (Firefox).
5. In the left sidebar, expand the **Cookies** section and select `https://www.instagram.com`.
6. Locate the cookie named `sessionid` and copy the value string.

![Session ID](session_id.png)

## Usage

1. Clone this repository or download the `ig-lookup.py` file.
2. Ensure you have installed the requirements.
3. Run the script via terminal:

```bash
python ig-lookup.py

```

4. Paste your `sessionid` when prompted.
5. Select your search mode:
* **Mode 1:** Search by User ID (Returns Profile URL)
* **Mode 2:** Search by Username (Returns User ID)



## Disclaimer

This tool is intended for educational purposes and legitimate research only. Use this script responsibly and in compliance with Instagram's Terms of Service. The author assumes no responsibility for any misuse of this software or potential account restrictions resulting from its use.

## License

This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) License](LICENSE.md).

## Author

* [@AyalX](https://github.com/AyalX)

## Contributions

Feedback is welcome! If you have suggestions for more features or find this tool useful, feel free to open an issue or star the repository. Please visit the [issues page](https://github.com/AyalX/Instagram-Lookup/issues) to submit feedback.
