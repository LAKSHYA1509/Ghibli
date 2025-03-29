from fastapi import FastAPI, File, UploadFile
import openai
from PIL import Image
import io

app = FastAPI()

# Set your OpenAI API Key
OPENAI_API_KEY = ""
openai.api_key = OPENAI_API_KEY

@app.post("/generate-ghibli/")
async def generate_ghibli(file: UploadFile = File(...)):
    # Load image
    image = Image.open(io.BytesIO(await file.read()))

    # Instead of sending image, modify prompt for DALL·E
    ghibli_prompt = (
        "A beautiful Studio Ghibli-style transformation of the uploaded image. "
        "Soft colors, anime aesthetic, dream-like atmosphere, and intricate details of the image to be taken into account."
    )

    # Call OpenAI's API
    response = openai.Image.create(
        model="dall-e-3",  # Using text-to-image instead
        prompt=ghibli_prompt,
        n=1,
        size="1024x1024"
    )

    return {"ghibli_image": response["data"][0]["url"]}
