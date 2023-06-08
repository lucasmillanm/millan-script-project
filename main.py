import os
from pytube import YouTube

def download_and_convert_audio_from_youtube():
    try:
        # Prompt the user to enter YouTube URL, output path, and file format
        youtube_url = input("Enter YouTube URL: ")
        output_path = input("Enter export path: ")
        file_format = input("Enter file format (MP4 or MP3): ").lower()

        # Create a YouTube object with the provided URL
        video = YouTube(youtube_url)

        if file_format == "mp4":
            # Download the video in MP4 format
            video_stream = video.streams.filter(progressive=True, file_extension='mp4').first()
            video_file = video_stream.download(output_path=output_path)
            print("Video downloaded successfully!")

            # Rename the downloaded file with the video's title
            output_file = os.path.join(output_path, f"{video.title}.mp4")
            os.rename(video_file, output_file)
            print("MP4 downloaded successfully!")
        elif file_format == "mp3":
            # Download the audio stream
            audio_stream = video.streams.filter(only_audio=True).first()
            audio_file = audio_stream.download(output_path=output_path)
            print("Audio downloaded successfully!")

            # Convert the downloaded audio to MP3 format
            convert_to_mp3_format(audio_file)
        else:
            print("Invalid file format. Please enter either MP4 or MP3.")
            return

    except Exception as e:
        print("Error: ", str(e))

def convert_to_mp3_format(input_file):
    # Get the output file path by replacing the file extension with .mp3
    mp3_file = os.path.splitext(input_file)[0] + ".mp3"
    os.rename(input_file, mp3_file)
    print("Converted to MP3 successfully!")

if __name__ == "__main__":
    download_and_convert_audio_from_youtube()
