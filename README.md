# Short Video Generator

**THIS DOCUMENT IS FOR _WINDOWS_ OPERATING SYSTEM ONLY**

*You can modify freely to match your device operating system*

## 1. Environment

Clone repository:
```
git clone https://github.com/Begineer17/Short-Video-Generator.git
```

You should create a new virtual environment to avoid conflicts with your current. You can use either **Python** or **Anaconda** to create a new environment.

**Python** :
```
python -m venv env
pip install -r requirements.txt
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
**Anaconda**:
```
conda create -n env python=3.10
pip install -r requirements.txt
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

**Notice**: Get and replace <YOUR_GEMINI_API> with your actual Gemini API key!!!
You can get it [here](https://ai.google.dev/gemini-api/docs/api-key) 

For combining video frames(.gif) and music(.wav) to video(.mp4) we using ffmpeg:
   * Step 1: Download packages at [link](https://ffmpeg.org/download.html).
   * Step 2: Unzip file and copy link 'bin' folder into PATH environment. 
   
For track generator: Click [here](https://1drv.ms/u/s!ArHNvccy1VzPkWGKXZDQY5k-kDi4?e=fFxcEq) to download the model checkpoint.

For converting beween .wav and .mid:
   * (.wav) -> (.mid):
      (command line) w2m melody.wav melody.mid
   * (.mid) -> (.wav):
      * * Step 1: download file zip fluidsynth version 2.3.5 at [here](https://github.com/FluidSynth/fluidsynth/releases/tag/v2.3.5), extract it and copy link 'bin' folder into PATH environment.
      * * Step 2: download file zip FluidRR3_GM.sf2 at [here](https://member.keymusician.com/Member/FluidR3_GM/index.html), extract it in this folder
      * * Step 3: (command line) fluidsynth -ni FluidR3_GM.sf2 melody.mid -F melody.wav

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

We develop advanced track change AI technology specifically designed to enhance and inspire user creativity. By leveraging state-of-the-art algorithms and innovative features, our AI tool provides users with seamless editing capabilities, encouraging creative expression and productivity

#### 2.22 Running

Run the generation script:
```
change_track.bat
```

The generation process is fast, and you can find the results saved as 'result/melody_changed.mid'. You can open it with [Musescore](https://musescore.com/) for further composition. 


### 3.Acknowledgement

We appreciate to the following authors who make their code and APIs available:

1. [Facebook/MusicGen](https://huggingface.co/facebook/musicgen-small)
2. [GeminiAPI](https://ai.google.dev/gemini-api/docs/api-key)
3. [ByteDance/AnimateDiff-Lightning](https://huggingface.co/ByteDance/AnimateDiff-Lightning)
4. [wangfuyun/AnimateLCM](https://huggingface.co/wangfuyun/AnimateLCM)
5. [Microsoft/Muzic/GetMusic](https://github.com/microsoft/muzic/tree/main/getmusic)
