import os
from pytube import YouTube

def download_audio_from_youtube():
    try:
        youtube_url = input("Enter YouTube URL: ")
        output_path = input("Enter output path: ")
        file_format = input("Enter file format (MP4 or MP3): ").lower()

        video = YouTube(youtube_url)

        if file_format == "mp4":
            video_stream = video.streams.filter(progressive=True, file_extension='mp4').first()
            video_file = video_stream.download(output_path=output_path)
            print("Video downloaded successfully!")

            output_file = os.path.join(output_path, f"{video.title}.mp4")
            os.rename(video_file, output_file)
            print("MP4 downloaded successfully!")
        elif file_format == "mp3":
            audio_stream = video.streams.filter(only_audio=True).first()
            audio_file = audio_stream.download(output_path=output_path)
            print("Audio downloaded successfully!")
            convert_to_mp3(audio_file)
        else:
            print("Invalid file format. Please enter either MP4 or MP3.")
            return

    except Exception as e:
        print("Error:", str(e))

def convert_to_mp3(input_file):
    mp3_file = os.path.splitext(input_file)[0] + ".mp3"
    os.rename(input_file, mp3_file)
    print("Converted to MP3 successfully!")

if __name__ == "__main__":
    download_audio_from_youtube()
