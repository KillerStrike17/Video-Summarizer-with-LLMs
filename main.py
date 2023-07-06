from transcription import transcription
from download_video import download_mp4_from_youtube
from deeplake_db import load_db
from video_summarizer import summarizer
import credentials
import os
from langchain.vectorstores import DeepLake

os.environ["OPENAI_API_KEY"] = credentials.openai
os.environ["ACTIVELOOP_TOKEN"] = credentials.active_loop

# urls=["https://www.youtube.com/watch?v=mBjPyte2ZZo&t=78s","https://www.youtube.com/watch?v=cjs7QKJNVYM",]
# videos_details = download_mp4_from_youtube(urls, 1)
# videos_details = [
#     ('./1+0.mp4', 'Filling the Gap in Large Language Models | Yann LeCun | Eye on AI #116', 'Eye on AI'), 
#     ('./1+1.mp4', '[ML News] Geoff Hinton leaves Google | Google has NO MOAT | OpenAI down half a billion', 'Yannic Kilcher')
#         ]
# # print(videos_details)

# filename = "text.txt"
# transcription(videos_details,filename)
# db = load_db(filename,credentials.active_loop_org_id, "video_summarizer_with_llms")

dataset_path = f"hub://{credentials.active_loop_org_id}/video_summarizer_with_llms"
db = DeepLake(dataset_path=dataset_path)

print(summarizer(db,"Summarize the mentions of google according to their AI program"))