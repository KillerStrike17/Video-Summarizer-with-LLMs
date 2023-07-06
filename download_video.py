import yt_dlp

def download_mp4_from_youtube(urls,job_id):
    
    video_info = []
    
    for i,url in enumerate(urls):
        
        file_temp = f'./{job_id}+{i}.mp4'
        ydl_opts = {
            "format":'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
            'outtmpl': file_temp,
            'quiet': True,
        }
        
        # Download the video file
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url, download= True)
            title = result.get("title","")
            author = result.get("uploader","")
        video_info.append((file_temp, title, author))
    
    return video_info



