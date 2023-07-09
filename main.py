from transcription import transcription
from download_video import download_mp4_from_youtube
from deeplake_db import load_db
from video_summarizer import summarizer
import credentials
import os
from langchain.vectorstores import DeepLake

# Set the environment variables for API keys
os.environ["OPENAI_API_KEY"] = credentials.openai
os.environ["ACTIVELOOP_TOKEN"] = credentials.active_loop

# Specify the YouTube video URLs to process
urls = ["https://www.youtube.com/watch?v=mBjPyte2ZZo&t=78s", "https://www.youtube.com/watch?v=cjs7QKJNVYM"]

# Download the videos and retrieve their details
videos_details = download_mp4_from_youtube(urls, 1)

print(videos_details)

# Specify the file name for the transcription
filename = "text.txt"

# Generate the transcription for the videos and save it to a file
transcription(videos_details, filename)

# Load the generated transcript into a DeepLake database
db = load_db(filename, credentials.active_loop_org_id, "video_summarizer_with_llms")

# Specify the dataset path for DeepLake
dataset_path = f"hub://{credentials.active_loop_org_id}/video_summarizer_with_llms"
db = DeepLake(dataset_path=dataset_path)

# Summarize the mentions of Google in the transcript using the loaded database
summary = summarizer(db, "Summarize the mentions of Google according to their AI program")
print(summary)
