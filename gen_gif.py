import torch
from diffusers import AnimateDiffPipeline, MotionAdapter, EulerDiscreteScheduler
from huggingface_hub import hf_hub_download
from safetensors.torch import load_file
import imageio  # Import imageio for GIF creation with FPS control

def generate_gif_cuda(prompt):
    device = "cuda"
    dtype = torch.float16

    step = 4 # Options: [1,2,4,8]
    repo = "ByteDance/AnimateDiff-Lightning"
    ckpt = f"animatediff_lightning_{step}step_diffusers.safetensors"
    base = "emilianJR/RealisticVision_V2"  # Choose to your favorite base model.

    # Use mixed precision and gradient checkpointing if supported
    adapter = MotionAdapter().to(device, dtype)
    adapter.load_state_dict(load_file(hf_hub_download(repo, ckpt), device=device))
    pipe = AnimateDiffPipeline.from_pretrained(base, motion_adapter=adapter, torch_dtype=dtype).to(device)
    pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config, timestep_spacing="trailing", beta_schedule="linear")

    # Reduce memory usage
    torch.cuda.empty_cache()

    # Use no_grad to save memory
    with torch.no_grad():
        output = pipe(
            # prompt="A space rocket with trails of smoke behind it launching into space from the desert, 4k, high resolution"
            prompt=f"{prompt}, 4k, high resolution",
            negative_prompt="bad quality, worse quality, low resolution",
            num_frames=16, 
            guidance_scale=2.0, 
            num_inference_steps=step)

    # Create a GIF with a higher FPS using imageio
    fps = 8  # Set the desired FPS for the GIF
    imageio.mimsave(f"result/animation.gif", output.frames[0], fps=fps)  # Save the GIF with the specified FPS
    return (f"result/animation.gif")

# Source: https://huggingface.co/wangfuyun/AnimateLCM
