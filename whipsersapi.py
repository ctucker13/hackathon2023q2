!pip install git+https://github.com/openai/whisper.git

!pip install yt-dlp
!yt-dlp https://www.youtube.com/watch?v=ens3BMKijPo --format m4a -o "%(id)s.%(ext)s"

!whisper "/content/ens3BMKijPo.m4a" --model small --language English
