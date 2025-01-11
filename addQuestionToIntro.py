from PIL import Image, ImageDraw, ImageFont
from textwrap import fill

# Load the image
input_image_path = "redditIntroImage.png"  # Replace with the image's path
output_image_path = "output_image_with_question.png"
image = Image.open(input_image_path)

# Initialize drawing context
draw = ImageDraw.Draw(image)

# Define the question text and font
question_text = "Why do some stories stand the test of time while others fade into obscurity?"
font_path = "Arial-Unicode-Regular.ttf"  # Replace with the path to your font file
font_size = 60  # Adjust for text size
font = ImageFont.truetype(font_path, font_size)

# Calculate text position and wrapping
text_wrap_width = 40  # Number of characters per line
paragraph_spacing = 20

# Split the text into wrapped lines
wrapped_text = fill(question_text, width=text_wrap_width)

# Calculate the size of the wrapped text using textbbox
text_bbox = draw.textbbox((0, 0), wrapped_text, font=font, spacing=paragraph_spacing)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# Get the dimensions of the image
image_width, image_height = image.size

# Calculate the position to center the text on the image
text_x = (image_width - text_width) // 2
text_y = (image_height - text_height) // 2

# Add the question text to the image
draw.text(
    (text_x, text_y),
    wrapped_text,
    font=font,
    fill="black",  # Adjust for contrast
    align="center",
    spacing=paragraph_spacing,
)

# Save the resulting image
image.save(output_image_path)
print(f"Image saved to {output_image_path}")
