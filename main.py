from instagrapi import Client
import os
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.environ.get("USERNAME_INFO")
PASSWORD = os.environ.get("PASSWORD")
# Login
cl = Client()
cl.login(USERNAME, PASSWORD)
# getting user_id from username for finding out the his/her followers
user_id = cl.user_id_from_username("rojinakhatiwada37")
print(user_id)
# finding out followers via user_id
followers = cl.user_followers(user_id)
print(followers)
