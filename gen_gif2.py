import torch
from diffusers import AnimateDiffPipeline, LCMScheduler, MotionAdapter
from diffusers.utils import export_to_gif

def generate_gif_cpu(prompt):
    adapter = MotionAdapter.from_pretrained("wangfuyun/AnimateLCM", torch_dtype=torch.float16)
    pipe = AnimateDiffPipeline.from_pretrained("emilianJR/epiCRealism", motion_adapter=adapter, torch_dtype=torch.float16)
    pipe.scheduler = LCMScheduler.from_config(pipe.scheduler.config, beta_schedule="linear")

    pipe.load_lora_weights("wangfuyun/AnimateLCM", weight_name="AnimateLCM_sd15_t2v_lora.safetensors", adapter_name="lcm-lora")
    pipe.set_adapters(["lcm-lora"], [0.8])

    pipe.enable_vae_slicing()
    pipe.enable_model_cpu_offload()

    output = pipe(
        # prompt="A space rocket with trails of smoke behind it launching into space from the desert, 4k, high resolution"
        prompt=f"{prompt}, 4k, high resolution",
        negative_prompt="bad quality, worse quality, low resolution",
        num_frames=16,
        guidance_scale=2.0,
        num_inference_steps=6,
        generator=torch.Generator("cpu").manual_seed(0),
    )
    frames = output.frames[0]

    export_to_gif(image=frames, output_gif_path=f"result/animation.gif", fps=8)
    return (f"result/animation.gif")

# Source: https://huggingface.co/ByteDance/AnimateDiff-Lightning