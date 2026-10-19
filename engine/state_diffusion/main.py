import PIL, torch, os
from diffusers import DiffusionPipeline
from huggingface_hub import notebook_login

from engine.state_hypervisor import hypervisor

DEVICE = "mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu"

if (DEVICE == "cpu") {
    hypervisor.CpuStatsConfigurator()
}
print(DEVICE)

pipe = DiffusionPipeline.from_pretrained("cagliostrolab/animagine-xl-4.0", dtype=torch.bfloat16, device_map="cuda")

def DiffusionPipeline(prompt: str):
    image = pipe(prompt).images[0]
    opened_image = PIL.ImageDraw(image)
    return opened_image