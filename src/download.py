import os
import yt_dlp

# Function to customize download options
def get_download_options():
    # Ensure the target directory exists
    download_dir = os.path.join("downloads",'')
    os.makedirs(download_dir, exist_ok=True)

    options = {
        'progress_hooks': [hook],  # Use a progress hook
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),  # Save with the video title in the directory
    }
    return options

# Progress hook to display download progress
def hook(d):
    if d['status'] == 'downloading':
        print(f"Downloading: {d['filename']} - {d['_percent_str']} complete")
    elif d['status'] == 'finished':
        print(f"\nDone downloading: {d['filename']}")

# Main download function
def download_video(url):
    ylt_opts = get_download_options()

    try:
        with yt_dlp.YoutubeDL(ylt_opts) as ydl:
            ydl.download([url])
        print("Downloading has completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    while True:
        url = input("Enter URL (or press 'q' to quit): ")
        
        if url.lower() == 'q':
            print("Exiting the program.")
            break
        download_video(url)
