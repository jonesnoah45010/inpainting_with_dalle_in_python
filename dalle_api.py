from openai import OpenAI
from PIL import Image
import requests
import os


os.environ["OPENAI_API_KEY"] = "YOUR_OPEN_AI_API_KEY_HERE"


client = OpenAI()

def inpaint_image(image_path, mask_path, prompt, save_file=True, output_path="inpainted_image.png"):
    """
    Performs inpainting on an image using DALL-E 2.

    Args:
        image_path: Path to the original image.
        mask_path: Path to the mask image (transparent areas indicate regions to inpaint).
        prompt: Text description of what to generate in the masked area.
        output_path: Path to save the inpainted image.
    """
    try:
        response = client.images.edit(
            model="dall-e-2",
            image=open(image_path, "rb"),
            mask=open(mask_path, "rb"),
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response.data[0].url
        if save_file:
            inpainted_image = Image.open(requests.get(image_url, stream=True).raw)
            inpainted_image.save(output_path)
            print(f"Inpainted image saved to {output_path}")
        return image_url

    except Exception as e:
         print(f"An error occurred: {e}")





def inpaint_image_in_memory(image_bytes, mask_bytes, prompt):
    """
    Performs inpainting on an image using DALL-E 2 with in-memory image data.

    Args:
        image_bytes: BytesIO object containing the original image.
        mask_bytes: BytesIO object containing the mask image.
        prompt: Text description of what to generate in the masked area.
        output_path: Path to save the inpainted image.
    Returns:
        image_url: string url that can be used to fetch the image
    """
    try:
        # Ensure the BytesIO objects are at the start
        image_bytes.seek(0)
        mask_bytes.seek(0)

        response = client.images.edit(
            model="dall-e-2",
            image=image_bytes,
            mask=mask_bytes,
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response.data[0].url
        return image_url

        # # Download and save the inpainted image
        # inpainted_image = Image.open(requests.get(image_url, stream=True).raw)
        # inpainted_image.save(output_path)
        # print(f"Inpainted image saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")




if __name__ == "__main__":

    inpaint_image("shpwedms.png", "shpwedms_mask.png", "give the frog a cowboy hat", "inpainted_image.png")

















