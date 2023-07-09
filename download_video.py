import yt_dlp

def download_mp4_from_youtube(urls: list, job_id: int):
    
    # Initialize a list to store video information
    video_info = []
    
    for i, url in enumerate(urls):
        
        # Set the file name for the downloaded video
        file_temp = f'./{job_id}+{i}.mp4'
        
        # Set the options for yt_dlp
        ydl_opts = {
            "format": 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
            'outtmpl': file_temp,
            'quiet': True,
        }
        
        # Download the video file
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url, download=True)
            title = result.get("title", "")
            author = result.get("uploader", "")
        
        # Append the video information to the list
        video_info.append((file_temp, title, author))
    
    return video_info