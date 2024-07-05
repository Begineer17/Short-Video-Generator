# Short Video Generator

**THIS DOCUMENT IS FOR WINDOWS OPERATING SYSTEM ONLY**
'You can modify freely to match your device operating system.'

## 1. Environment

<!-- You can use python virtual enviroment or anaconda, but make sure to install python <=  -->

Python environment:
```
pip install -r requirements.txt
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
**Notice**: Get and replace <YOUR_GEMINI_API> with your actual Gemini API key!!! 

For combining video frames(.gif) and music(.wav) to video(.mp4) we using ffmpeg:
   * Step 1: Download packages at link: https://ffmpeg.org/download.html.
   * Step 2: Unzip file and copy link 'bin' folder into PATH environment. 
   
For track generator: 
   Click [here](https://1drv.ms/u/s!ArHNvccy1VzPkWGKXZDQY5k-kDi4?e=fFxcEq) to download the model checkpoint.

For converting beween .wav and .mid:
   * (.wav) -> (.mid):
      (command line) w2m melody.wav melody.mid
   * (.mid) -> (.wav):
      Step 1: download file zip fluidsynth, extract it and go to the folder, copy the path and path to PATH of system environment
      Step 2: (command line) fluidsynth -ni FluidR3_GM.sf2 melody.mid -F melody.wav

## 2. Inference

### 2.1 Video and Music Generation

#### 2.11 Usage

Utilize the TikTok API to retrieve the user's most viewed video, leveraging this data to generate a new video focused on the natural environment. This initiative seeks to celebrate and pay homage to the exquisite beauty of our planet, aiming to inspire environmental consciousness and appreciation among viewers through engaging and relevant content creation.

#### 2.12 Running

Run the generation script:
```
make_original_video.bat
```

### 2.2 Track Change

**Notice**: Still under improvement.

#### 2.21 Usage

To facilitate an environment conducive to maximizing user creativity, we aim to provide tools, resources, and support that inspire innovation and imagination. Our goal is to empower users with the means to explore their creative potential fully and to achieve their creative aspirations effectively.

#### 2.22 Running

Run the generation script:
```
change_track.bat
```

The generation process is fast, and you can find the results saved as 'example_data/inference/lc2dgp-childhood.mid'. You can open it with [Musescore](https://musescore.com/) for further composition. 


### 3.Acknowledgement

We appreciate to the following authors who make their code and APIs available:

1. [Facebook/MusicGen](https://huggingface.co/facebook/musicgen-small)
2. [GeminiAPI](https://ai.google.dev/gemini-api/docs/api-key)
3. [ByteDance/AnimateDiff-Lightning](https://huggingface.co/ByteDance/AnimateDiff-Lightning)
4. [wangfuyun/AnimateLCM](https://huggingface.co/wangfuyun/AnimateLCM)
5. [Microsoft/Muzic/GetMusic](https://github.com/microsoft/muzic/tree/main/getmusic)