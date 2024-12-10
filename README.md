# Mela YouTube Video Downloader

This Python script allows you to download videos from YouTube using the powerful `yt-dlp` library. It features a user-friendly interface and progress updates during downloads.

## Features

- **Progress Display:** See the current download status, including percentage completed.
- **Automatic File Naming:** Saves the video with its title as the file name.
- **Error Handling:** Gracefully handles errors during the download process.

## Requirements

- Python 3.7 or higher
- The `yt-dlp` library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your-repository
   ```
3. Install `yt-dlp`:
   ```bash
   pip install yt-dlp
   ```

## Usage

1. Run the script:
   ```bash
   python yt_downloader.py
   ```
2. Enter the URL of the YouTube video you want to download.
3. To exit the program, type `q`.

## Example

```plaintext
Enter URL (or press 'q' to quit): https://www.youtube.com/watch?v=example
Downloading: Example Video Title - 45% complete
Downloading: Example Video Title - 100% complete

Done downloading: Example Video Title.mp4
Downloading has completed successfully!
```

## Notes

- Ensure that the URL is valid and accessible.
- The downloaded file will be saved in the same directory as the script.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp): A fantastic tool for downloading videos from various platforms.
