w2m result/melody.wav result/melody.mid

python track_genration.py --load_path checkpoint.pth --file_path result

fluidsynth -ni FluidR3_GM.sf2 result/melody_changed.mid -F result/melody_changed.wav

ffmpeg -i result/melody_changed.wav -stream_loop -1 -i result/animation.gif -shortest -map 0:a -map 1:v -c:v libx264 -pix_fmt yuv420p -c:a aac -b:a 192k result/output_changed.mp4