#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pendulum
print(f"Execution started at {pendulum.now().to_datetime_string()}")


# In[14]:


import argparse
import pandas as pd
import json
import time
import requests
import sys
sys.path.insert(1, '/home/ubuntu/')


# In[15]:


def upload_video(video_url,access_token,ig_user_id,caption):
    post_url =f"https://graph.facebook.com/v19.0/{ig_user_id}/media"
    payload = {
        "media_type":"REELS",
        "video_url":video_url,
        "caption":caption,
        "access_token":access_token
    }
    r = requests.post(post_url,data=payload)
    result = json.loads(r.text)
    return(result)


# In[16]:


def upload_video_to_instagram(creation_id,access_token, instagram_account_id):
    # Step 2: Publish the video using the container
    publish_url = f"https://graph.facebook.com/v19.0/{instagram_account_id}/media_publish"
    publish_payload = {
        'creation_id': creation_id,
        'access_token': access_token
    }
    publish_response = requests.post(publish_url, data=publish_payload).json()

    return publish_response


# In[17]:


def upload_file_to_0x0st(file_path):
    with open(file_path, 'rb') as f:
        response = requests.post('https://0x0.st', files={'file': f})
    if response.status_code == 200:
        return response.text.strip()
    else:
        raise Exception("Failed to upload file")


# In[18]:


# import os
# import random

# def delete_file(file_path):
#     try:
#         os.remove(file_path)
#         print(f"File '{file_path}' deleted successfully.")
#     except OSError as e:
#         print(f"Error deleting the file '{file_path}': {e}")


# In[19]:


# folder_path = '/home/ubuntu/youtube/islamicVideo/'
# files = os.listdir(folder_path)
# if files:
#     # Select a random file
#     random_file_name = random.choice(files)
#     video_file_path = os.path.join(folder_path, random_file_name)
# else:
#     sys.exit()


# In[38]:


df=pd.read_csv("instagram/islamicShorts.csv")


# In[ ]:


video_file_path = df["path"][0]


# In[20]:


try:
    video_url = upload_file_to_0x0st(video_file_path)
    print("Video URL:", video_url)
except Exception as e:
    print(e)


# In[21]:


caption = """Follow & support 
#IslamicQuotes #Inspiration #Faith #Resilience #Gratitude #IslamicWisdom #Spirituality #IslamicInsights"""


# In[25]:


ig_user_id = "17841465397818189"
access_token = "EAAObxuixsnIBOxZBPdE4plUc2yZB6H4QKhmZAykLLV9pjOdkqnnSu9oWMQuAQMtDboN01tap2JO8yadZB70Vg11zjGZAAFOM9W2j9SOQNSfcIwpOMT2Pdv2cVumUtuWKfREAHimbZB5ZAXcYf7gZCNWgU4WBfWrXpsIFbVvp1LBUORTQhpoTZCrkZAlZC3k"


# In[26]:


result = upload_video(video_url,access_token,ig_user_id,caption)
creation_id = result["id"]
time.sleep(60)


# In[27]:


upload_video_to_instagram(creation_id,access_token, ig_user_id)


# In[ ]:


df[1:].to_csv("instagram/islamicShorts.csv",index=False)


# In[28]:


# delete_file(video_file_path)


# In[33]:


print(f"Execution ended at {pendulum.now().to_datetime_string()}")


# In[ ]:




