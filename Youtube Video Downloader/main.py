import yt_dlp

def download_video(url, resolution='highest'):
    try:
        # Set yt-dlp options for video download
        ydl_opts = {
            'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]' if resolution != 'highest' else 'best',
            'outtmpl': '%(title)s.%(ext)s',  # Output file name template
        }

        # Download video with yt-dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    video_url = input("Enter YouTube URL: ")
    video_resolution = input("Enter resolution (e.g., 720p or leave blank for highest): ").strip()

    # Download the video with specified resolution
    download_video(video_url, video_resolution or 'highest')
