import runpod
from inference import generate_video

def handler(event):
    input_data = event.get("input", {})
    prompt = input_data.get("prompt", "A cinematic scene")

    video_path = generate_video(prompt)

    return {
        "status": "success",
        "video": video_path
    }

runpod.serverless.start({"handler": handler})