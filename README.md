# Video Summarizer

This project aims to summarize the content of YouTube videos by performing transcription and generating concise summaries based on the transcriptions. It utilizes various modules and APIs for tasks such as video downloading, transcription, database management, and summarization.

## Prerequisites

Before running the code, make sure you have the following prerequisites:

- Python 3.x
- API keys or credentials for the required services:
  - OpenAI API key
  - ActiveLoop token

## Installation

1.  Clone the repository:

        `git clone https://github.com/your-repo/video-summarizer.git`

2.  Install the required Python packages:

        `pip install -r requirements.txt`

3.  Set up environment variables:

Set the following environment variables with the respective API keys and credentials:

- `OPENAI_API_KEY`: Your OpenAI API key
- `ACTIVELOOP_TOKEN`: Your ActiveLoop token

## Usage

The code consists of several modules and scripts. Below is an overview of each component and how to use it:

### 1. Downloading YouTube Videos

The `download_video.py` script is responsible for downloading YouTube videos and retrieving their details. To use it, follow these steps:

1. Provide a list of YouTube video URLs in the `urls` variable.
2. Call the `download_mp4_from_youtube(urls, job_id)` function, passing the video URLs and a unique job ID.
3. The script will download the videos and return a list of video details, including the downloaded file paths, titles, and authors.

### 2. Transcription

The `transcription.py` module handles the transcription of videos. To transcribe the videos, do the following:

1. Ensure you have the video details, either obtained from the previous step or manually specified in the `videos_details` variable.
2. Call the `transcription(videos_details, filename)` function, providing the video details and the desired file name for the transcription.
3. The module will split the videos into smaller chunks and transcribe them. The transcriptions will be saved in the specified file.

### 3. DeepLake Database

The `deeplake_db.py` module is responsible for managing the DeepLake database. To load the transcriptions into the database, follow these steps:

1. Provide the file name of the transcription in the `filename` variable.
2. Call the `load_db(filename, my_activeloop_org_id, database_name)` function, passing the transcription file name, ActiveLoop organization ID, and the desired database name.
3. The module will load the transcriptions into the DeepLake database, creating a dataset at the specified organization ID and database name.

### 4. Video Summarization

The `video_summarizer.py` script performs video summarization based on the transcriptions stored in the DeepLake database. To generate a summary, do the following:

1. Ensure you have loaded the transcriptions into the DeepLake database using the previous step.
2. Specify the desired query in the `query` variable.
3. Call the `summarizer(db, query)` function, passing the DeepLake database object and the query.
4. The script will utilize the database to summarize the content based on the query and return the summarized results.
