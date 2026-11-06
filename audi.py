import yt_dlp 
url= input("url del video: ")
op={
    'format': 'bestaudio/best', 
    "outtmpl": r"C:\\Users\\Casa\\Music\\%(title)s.%(ext)s",
    "ffmpeg_location": r"C:\\Users\\Casa\\Downloads\\ffmpeg-6.0-full_build\\bin\\ffmpeg.exe",
    "postprocessors" : [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '190',
    }],
}
try:
    with yt_dlp.YoutubeDL(op) as ydl:
        ydl.download([url])
    print("descarga completada | mira la carpeta musica")
except Exception as e:
    print(f"ocurrió un error: {e}")
