from PIL import Image, ImageDraw, ImageFont # type: ignore

# Create an 800x800 pixel image with a solid background color
image_size = (800, 800)
background_color = (35, 35, 35)  # Dark grey background
image = Image.new('RGB', image_size, background_color)

# Initialize ImageDraw
draw = ImageDraw.Draw(image)

# Load a bold font
try:
    # Attempt to use a default bold font from PIL
    font = ImageFont.truetype("DejaVuSans-Bold.ttf", 150)
except IOError:
    # Fallback to a default PIL font if the specified one isn't found
    font = ImageFont.load_default()

# Define the text and get its size using textbbox
text = "Factory"
text_color = (255, 204, 0)  # Industrial yellow color
text_bbox = draw.textbbox((0, 0), text, font=font)
text_size = (text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1])

# Calculate the position to center the text
text_position = ((image_size[0] - text_size[0]) / 2, (image_size[1] - text_size[1]) / 2 - 50)

# Add the text to the image
draw.text(text_position, text, font=font, fill=text_color)

# Draw gears (simplified as circles for this example)
gear_color = (192, 192, 192)  # Light grey for gears
gear_positions = [
    (100, 600, 200, 700),  # Bottom-left
    (600, 100, 700, 200),  # Top-right
]

for pos in gear_positions:
    draw.ellipse(pos, fill=gear_color)

# Save the image to a file
image_path = "/Desktop/Factory_Logo.png"
image.save(image_path)

image_path