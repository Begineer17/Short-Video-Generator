from gen_melody import *
from gen_gif import *
from gen_gif2 import *
from gen_text import *
import sys

prompt_video, prompt_melody = generate_prompt_from_hashtags()

if prompt_melody == prompt_video == None: sys.exit()

if torch.cuda.is_available():
    gif_path = generate_gif_cuda(prompt=prompt_video)
else:
    gif_path = generate_gif_cpu(prompt=prompt_video)

melody_path = generate_melody(prompt=prompt_melody)



# Command line to combine melody and gif: ffmpeg -i result/melody.wav -stream_loop -1 -i result/animation.gif -shortest -map 0:a -map 1:v -c:v libx264 -pix_fmt yuv420p -c:a aac -b:a 192k result/output.mp4

# .wav to .mid
# Step 1: pip install sound-to-midi, librosa, midiutil
# Step 2: (command line) w2m melody.wav melody.mid
# 
# .mid to .wav 
# Step 1: download file zip fluidsynth, extract it and go to the folder, copy the path and path to PATH of system environment
# Step 2: download file zip FluidRR3_GM.sf2, extract
# Step 3: (command line) fluidsynth -ni FluidR3_GM.sf2 melody.mid -F melody.wav
#fluidsynth -ni FluidR3_GM.sf2 result/melody_changed.mid -F result/melody_changed.wav