python main.py

ffmpeg -i result/melody.wav -stream_loop -1 -i result/animation.gif -shortest -map 0:a -map 1:v -c:v libx264 -pix_fmt yuv420p -c:a aac -b:a 192k result/output.mp4