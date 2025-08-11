import os
from PIL import Image

# Ask for new dimensions
width = int(input("Enter new width: "))
height = int(input("Enter new height: "))

input_folder = "images_input"
output_folder = "images_output"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Function to check transparency
def has_transparency(img):
    if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
        return True
    return False

# Loop through images
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Resize
        img_resized = img.resize((width, height))

        # Decide format
        if has_transparency(img_resized):
            output_format = "PNG"
            ext = "png"
        else:
            output_format = "JPEG"
            ext = "jpg"

        # Save
        base_name = os.path.splitext(filename)[0]
        save_path = os.path.join(output_folder, f"{base_name}.{ext}")
        img_resized.save(save_path, output_format)
        print(f"✅ {filename} → {ext.upper()} saved at {save_path}")

print("🎯 All images resized and saved with optimal formats!")
