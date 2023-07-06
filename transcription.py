import whisper


def transcription(videos_details,filename):
    # load the model
    model = whisper.load_model("base")

    #Iterate through each video and transcribe
    results = []
    for video in videos_details:
        result = model.transcribe(video[0])
        results.append(result['text'])
        print(f"Transcription for {video[0]}:\n{result['text']}\n")

    with open(filename,'w') as file:
        file.write("\n\n\n".join(results))
        
