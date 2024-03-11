# Import necessary libraries
import pendulum  # Timezone-aware datetime library
print(f"Execution started at {pendulum.now().to_datetime_string()}")  # Print the start time of the execution

# Additional necessary libraries
import argparse  # Parser for command-line options, arguments and sub-commands
import pandas as pd  # Data manipulation and analysis library
import json  # Library for JSON encoding and decoding
import time  # Time access and conversions
import requests  # HTTP library

# Function to upload a video to Instagram
def upload_video(video_url,access_token,ig_user_id,caption):
    post_url = f"https://graph.facebook.com/v19.0/{ig_user_id}/media"  # Endpoint for Instagram Media Publish API
    payload = {
        "media_type": "REELS",  # Specify the media type
        "video_url": video_url,  # URL of the video to upload
        "caption": caption,  # Caption for the video
        "access_token": access_token  # Access token for authentication
    }
    r = requests.post(post_url, data=payload)  # POST request to upload the video
    result = json.loads(r.text)  # Convert the response to JSON format
    return result  # Return the result of the upload

# Function to publish the video on Instagram using the media publish endpoint
def upload_video_to_instagram(creation_id, access_token, instagram_account_id):
    publish_url = f"https://graph.facebook.com/v19.0/{instagram_account_id}/media_publish"  # Instagram Media Publish endpoint
    publish_payload = {
        'creation_id': creation_id,  # The creation ID obtained from the upload
        'access_token': access_token  # Access token for authentication
    }
    publish_response = requests.post(publish_url, data=publish_payload).json()  # POST request to publish the video
    return publish_response  # Return the publish response

# Function to upload a file to the 0x0.st file hosting service
def upload_file_to_0x0st(file_path):
    with open(file_path, 'rb') as f:  # Open the file in binary read mode
        response = requests.post('https://0x0.st', files={'file': f})  # POST request to upload the file
    if response.status_code == 200:  # Check if the request was successful
        return response.text.strip()  # Return the response text
    else:
        raise Exception("Failed to upload file")  # Raise an exception if upload failed

# Read CSV file containing paths to videos and their captions
df = pd.read_csv("instagram/Shorts.csv")  # Load the CSV file into a pandas DataFrame

video_file_path = df["path"][0]  # Get the path of the first video file

# Try to upload the video file and print the URL or catch and print any errors
try:
    video_url = upload_file_to_0x0st(video_file_path)  # Upload the video file and get the URL
    print("Video URL:", video_url)  # Print the video URL
except Exception as e:
    print(e)  # Print the error

caption = caption  # Set the video caption
ig_user_id = ig_user_id  # Set the Instagram User ID
access_token = access_token  # Set the access token

# Upload the video to Instagram and obtain the creation ID
result = upload_video(video_url, access_token, ig_user_id, caption)  # Call the upload_video function
creation_id = result["id"]  # Extract the creation ID from the result
time.sleep(60)  # Wait for 60 seconds

# Call the function to publish the video on Instagram
upload_video_to_instagram(creation_id, access_token, ig_user_id)  # Publish the video

# Update the CSV file to remove the first line (the video that was just uploaded)
df[1:].to_csv("instagram/Shorts.csv", index=False)  # Save the updated DataFrame to CSV

# Print the end time of the execution
print(f"Execution ended at {pendulum.now().to_datetime_string()}")
