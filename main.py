from make_mask import generate_mask
from dalle_api import inpaint_image


if __name__ == "__main__":
    image_path = "shpwedms.png" # source image to be edited should be "1024x1024"
    mask_path = "shpwedms_mask.png" # name of mask file to be created
    prompt = "give the frog a cowboy hat" # prompt to use to do the editing
    coordinates = [(420, 25), (620, 25), (620, 300), (420, 300)]  # square area to edit as (x,y) coordinates
    output_path = "shpwedms_inpainted.png" # new file created upon editing finishing
    generate_mask(image_path, mask_path, coordinates) # creates the mask from the source image
    image_url = inpaint_image(image_path, mask_path, prompt, output_path) # executes the inpainting/editing
    print(image_url) # image can be accessed from the local file or from the url




