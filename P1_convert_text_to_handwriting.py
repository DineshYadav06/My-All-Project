from PIL import Image, ImageDraw, ImageFont
import textwrap

txt = """Dinesh Kumar Yadav is a curious and driven tech enthusiast with a passion for coding, learning, and creating. From exploring Python projects to mastering GitHub workflows, he thrives on turning ideas into reality and solving challenges with a mix of logic and creativity. Always eager to experiment and grow, Dinesh approaches each day as an opportunity to learn something new, embrace mistakes as stepping stones, and push the boundaries of his skills. With a playful yet focused mindset, he balances serious problem-solving with a love for innovation, proving that curiosity, dedication, and a spark of fun can lead to amazing things."""

# Create a blank white image
img = Image.new("RGB", (1200, 800), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

font_path = r"C:\Windows\Fonts\segoesc.ttf" 
font = ImageFont.truetype(font_path, 24)

# Draw text with line wrapping
lines = textwrap.wrap(txt, width=60)
y_text = 50
for line in lines:
    draw.text((50, y_text), line, font=font, fill=(0, 0, 255))
    y_text += 30

# Save the image
img.save("dkt_offline.png")
print("Handwriting image saved as dkt_offline.png")
