import requests
import time
import random


# SESSIONID, DS_USER_ID, and CSRFTOKEN, you can find in F12 > Application > Cookie > instagram.com
# F12 must be pressed on your own user page (EXAMPLE: https://instagram.com/my_user)


SESSIONID = "YOUR SESSION ID"
DS_USER_ID = "YOUR DS USER ID"
CSRFTOKEN = "YOUR CSRF TOKEN"
MAX_UNFOLLOWS = 100  # Number of followers you want to remove
DELAY_MIN = 1
DELAY_MAX = 10
MAX_RETRIES = 3

headers = {
    'cookie': f'sessionid={SESSIONID}; ds_user_id={DS_USER_ID}; csrftoken={CSRFTOKEN}',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'x-ig-app-id': '936619743392459',
    'x-csrftoken': CSRFTOKEN,
    'x-requested-with': 'XMLHttpRequest'
}


def get_following_list():
    url = f'https://www.instagram.com/api/v1/friendships/{DS_USER_ID}/following/?count=50'

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return [user['pk'] for user in response.json().get('users', [])]
        else:
            print(f"Error {response.status_code}. Response:", response.text)
            return []
    except Exception as e:
        print(f"Error on request: {str(e)}")
        return []


def unfollow_user(user_id):
    url = f'https://www.instagram.com/api/v1/friendships/destroy/{user_id}/'

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.post(url, headers=headers)
            if response.status_code == 200:
                return True
            else:
                print(f"Attempt {attempt + 1} failed. Error {response.status_code}")
                time.sleep(random.uniform(5, 15))
        except Exception as e:
            print(f"Error on attempt {attempt + 1}: {str(e)}")
            time.sleep(random.uniform(5, 15))

    return False


def main():
    print("[START] Starting unfollow process...")
    unfollowed_total = 0

    while unfollowed_total < MAX_UNFOLLOWS:
        print("\n[*] Getting list of accounts you follow...")
        following_ids = get_following_list()

        if not following_ids:
            print("[-] Unable to get list of following accounts. Retrying in 60 seconds...")
            time.sleep(60)
            continue

        print(f"[*] You Follow {len(following_ids)} accounts. Processing...")

        for user_id in following_ids:
            if unfollowed_total >= MAX_UNFOLLOWS:
                break

            if unfollow_user(user_id):
                unfollowed_total += 1
                delay = random.uniform(DELAY_MIN, DELAY_MAX)
                print(f"[+] Unfollow {unfollowed_total}/{MAX_UNFOLLOWS}. Next attempt {delay:.1f}s...")
                time.sleep(delay)
            else:
                print(f"[-] Failed to unfollow user {user_id}. Continuing...")
                time.sleep(30)

        if unfollowed_total < MAX_UNFOLLOWS:
            wait_time = random.uniform(60, 120)
            print(
                f"[*] Reached the end of the current list. Waiting {wait_time:.1f} seconds before checking again...")
            time.sleep(wait_time)

    print(f"\n[END] Process completed. Total left to follow: {unfollowed_total}")


if __name__ == "__main__":
    main()
