from RedDownloader import RedDownloader
from instagrapi import Client

import time
import os
import random

subreddit = open('subreddit.js', 'r').read()
password = open('password.js', 'r').read()
output = open('output.txt', 'r').read()
sort_by = open('sort_by.txt', 'r').read()
instagram_page = open('instagram_page.js', 'r').read()


# Fetch posts from Reddit
def get_post():
    post = RedDownloader.DownloadBySubreddit(subreddit, 1, output=output, SortBy=sort_by)
    authors = post.GetPostAuthors()[0]
    return authors


# Login to Instagram
client = Client()
client.login(instagram_page, password)


# Decide on post captions
def create_caption():
    captions = [
        ''
        ''
        ''
        ''
        ''
    ]
    return random.choice(captions)


# Delete posts from the output folder once they have been posted to avoid collisions.
def delete_posts():
    try:
        os.remove(f'{output}/{output + "1"}.jpeg')
    except:
        pass


# Upload the post taken from Reddit
while True:
    author = get_post()
    hashtags = create_caption()

    caption = f'Credits to the original poster u/{author} on Reddit. \n {hashtags}'

    try:
        client.photo_upload(f'{output}/{output + "1"}.jpeg', caption)

    except Exception as exception:
        print(exception)

    finally:
        print('Process completed.')

    # Post with 30 to 60 minutes time interval
    minutes_to_sleep = random.randint(30, 60)

    # Put bot to the sleep to avoid possible bot detections
    time.sleep(minutes_to_sleep * 60)
    delete_posts()
