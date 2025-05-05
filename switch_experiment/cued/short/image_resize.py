import os
from PIL import Image

def resize_images_inplace(scale_factor, base_dir='.'):
    for root, dirs, files in os.walk(base_dir):
        for filename in files:
            if filename.lower().endswith('.png'):
                file_path = os.path.join(root, filename)
                try:
                    with Image.open(file_path) as img:
                        orig_width, orig_height = img.size
                        new_width = int(orig_width * scale_factor)
                        new_height = int(orig_height * scale_factor)
                        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
                        # Save the resized image in place (overwriting the original)
                        resized_img.save(file_path)
                        print(f"Processed {file_path}")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

scale_factor = float(input("Enter the scale factor (e.g. 0.3): "))
resize_images_inplace(scale_factor)
