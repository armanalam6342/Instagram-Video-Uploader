import pendulum
print(f"Execution started at {pendulum.now().to_datetime_string()}")


import argparse
import pandas as pd
import json
import time
import requests
import sys
sys.path.insert(1, '/home/ubuntu/')



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



def upload_video_to_instagram(creation_id,access_token, instagram_account_id):
    # Step 2: Publish the video using the container
    publish_url = f"https://graph.facebook.com/v19.0/{instagram_account_id}/media_publish"
    publish_payload = {
        'creation_id': creation_id,
        'access_token': access_token
    }
    publish_response = requests.post(publish_url, data=publish_payload).json()

    return publish_response



def upload_file_to_0x0st(file_path):
    with open(file_path, 'rb') as f:
        response = requests.post('https://0x0.st', files={'file': f})
    if response.status_code == 200:
        return response.text.strip()
    else:
        raise Exception("Failed to upload file")



df=pd.read_csv("instagram/Shorts.csv")


video_file_path = df["path"][0]



try:
    video_url = upload_file_to_0x0st(video_file_path)
    print("Video URL:", video_url)
except Exception as e:
    print(e)


caption = caption


ig_user_id = ig_user_id
access_token = access_token


result = upload_video(video_url,access_token,ig_user_id,caption)
creation_id = result["id"]
time.sleep(60)



upload_video_to_instagram(creation_id,access_token, ig_user_id)



df[1:].to_csv("instagram/Shorts.csv",index=False)


print(f"Execution ended at {pendulum.now().to_datetime_string()}")


# In[ ]:




