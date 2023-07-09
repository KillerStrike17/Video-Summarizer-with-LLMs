import whisper


def transcription(videos_details: list, filename: str):
    # Load the model
    model = whisper.load_model("base")

    # Iterate through each video and transcribe
    results = []
    for video in videos_details:
        # Transcribe the video
        result = model.transcribe(video[0])
        results.append(result['text'])
        # Print the transcription for each video
        print(f"Transcription for {video[0]}:\n{result['text']}\n")

    # Write the transcriptions to a file
    with open(filename, 'w') as file:
        file.write("\n\n\n".join(results))