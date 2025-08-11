# Batch-Image-Resizer

## Objective

A Python tool to batch resize and convert images, automatically choosing the best format based on transparency, using Pillow.

## Features

* **Batch Processing** – resize all images in a folder at once.
* **Automatic Format Selection** – saves as **PNG** if transparency is detected, otherwise **JPG** for smaller size.
* **Custom Dimensions** – enter any width and height at runtime.
* Supports multiple formats: PNG, JPG, JPEG, BMP, GIF.

## Installation

```
pip install pillow
```

## Usage

1. Create a folder named **images\_input** and place your images inside.
2. Run the script:

   ```
   python image_resizer.py
   ```
3. Enter your desired width and height when prompted.
4. Resized images will be saved in **images\_output** with the optimal format.

## Example

```
Enter new width: 800
Enter new height: 600
✅ sample_1.jpg → JPG saved at images_output/sample_1.jpg
✅ logo.png → PNG saved at images_output/logo.png
```

## Output

* If image has **transparency** → saved as **PNG**.
* If no transparency → saved as **JPG** for smaller file size.

## Outcome

Efficiently resize and convert images in bulk while preserving quality and optimizing storage.
