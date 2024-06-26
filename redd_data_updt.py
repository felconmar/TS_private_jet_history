# import the modules
import os
import re

import praw
from dotenv import load_dotenv
import pandas as pd


load_dotenv()

# initialize with appropriate values
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
username = os.getenv("username")
password = os.getenv("password")
user_agent = "TS Private Jet"

user_name = os.getenv("user_name")

def remove_emojis(input_string):
    emoji_pattern = re.compile(
        "["
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"  # alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "]+"
    )
    return emoji_pattern.sub("", input_string)

# creating an authorized reddit instance
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)


user = reddit.redditor(user_name)
submissions = user.submissions.new(limit=5)
for submission in submissions:
    print(submission.created_utc)
    print(submission.author)
    print(submission.subreddit)
    print(submission.title)
    print(submission.url)
    print(submission.permalink)
    print("-----------------------------------------------")