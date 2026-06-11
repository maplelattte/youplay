import yt_dlp
from colorama import Fore, Style, init
from mutagen.easyid3 import EasyID3

init(autoreset=True)

def download_progress_hook(d):
    """Callback function to show real-time download status."""
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '0.0%')
        print(f"{Fore.CYAN}Downloading: {percent} completed...", end='\r')
    elif d['status'] == 'finished':
        print(f"{Fore.GREEN}\nConversion to MP3 started...")

def get_downloader_options(output_path='./downloads'):
    """Returns the configuration dictionary for yt-dlp."""
    return {
        'format': 'bestaudio/best',
        'noplaylist': False,
        'progress_hooks': [download_progress_hook],
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'ignoreerrors': True,
    }

def download_playlist(playlist_url):
    """Main function to trigger the download."""
    opts = get_downloader_options()
    print(f"{Fore.YELLOW}Analyzing playlist. Please Wait...")
    with yt_dlp.YoutubeDL(opts) as ydl:
        try:
            ydl.download([playlist_url])
            print(f"{Fore.GREEN}All downloads and conversions completed!")
        except Exception as e:
            print(f"{Fore.RED}An error occurred: {e}")

def add_mp3_metadata(file_path, title, artist="Unknown Artist"):
    """Injects metadata tags directly into the downloaded MP3 file."""
    try:
        audio = EasyID3(file_path)
        audio['title'] = title
        audio['artist'] = artist
        audio.save()
        print(f"Successfully tagged: {title}")
    except Exception as e:
        print(f"Could not tag file: {e}")

# Test execution block
import argparse

# ... (Keep all your existing functions exactly as they are) ...

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=f"{Fore.GREEN}Youplay - Helps in downloading playlists to local machines :D"
    )
    
    parser.add_argument(
        '-u', '--url', 
        type=str, 
        required=True, 
        help="The URL of the YouTube or YouTube Music playlist/video"
    )
    parser.add_argument(
        '-o', '--output', 
        type=str, 
        default='./downloads', 
        help="The directory where MP3 files should be saved (Default: ./downloads)"
    )

    args = parser.parse_args()

    print(f"{Fore.BLUE}Target Output Directory: {args.output}")
    download_playlist(args.url)
