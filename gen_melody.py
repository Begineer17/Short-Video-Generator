from transformers import MusicgenProcessor, MusicgenForConditionalGeneration
# import torchaudio
import scipy

def generate_melody(prompt):
    # Load the processor and model
    processor = MusicgenProcessor.from_pretrained("facebook/musicgen-small")
    model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")

    # Prepare input text
    # input_text = "A calm and soothing piano melody"

    # Generate music
    inputs = processor(text=prompt, return_tensors="pt")
    music = model.generate(**inputs, max_new_tokens=800)

    # Save the generated music
    # torchaudio.save("generated_music.wav", music["waveform"], sample_rate=music["sample_rate"])

    sampling_rate = model.config.audio_encoder.sampling_rate
    scipy.io.wavfile.write(f"result/melody.wav", rate=sampling_rate, data=music[0, 0].numpy())
    return (f"result/melody.wav")

# Source: https://huggingface.co/facebook/musicgen-small