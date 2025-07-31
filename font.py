from PIL import ImageFont, ImageDraw, Image
import cv2
import numpy as np

# Load font (you can specify your own .ttf file)
fontpath = '/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf'  # Change path for Windows/Mac
font = ImageFont.truetype(fontpath, 70)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to PIL image
    pil_im = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_im)
    draw.text((50, 50), "Live Camera Feed", font=font, fill=(0, 255, 0))  # RGB color

    # Convert back to OpenCV format
    frame = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

    cv2.imshow("High-Quality Text", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
