from pytube import YouTube
link= input ("Enter URL of the video")
video= YouTube(link)
stream= video.streams.get_highest_resolution()
stream.download()