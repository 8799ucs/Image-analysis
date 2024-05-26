import cv2
from PIL import Image
import numpy as np
import pytesseract

def extract_text(image_path):
  # Read the image
  img = Image.fromarray(image_path)

  # Extract text using Tesseract OCR
  text = pytesseract.image_to_string(img)
  return text

def threshold_segmentation(image):
  # Convert image to grayscale
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Apply thresholding (adjust threshold value based on your image)
  thresh, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

  # Find contours of the object
  contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # Assuming there's only one object, extract largest contour
  if len(contours) > 0:
    largest_contour = max(contours, key=cv2.contourArea)
    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.drawContours(mask, [largest_contour], -1, 255, -1)

    # Apply mask to extract object
    extracted_object = cv2.bitwise_and(image, image, mask=mask)
    return extracted_object
  else:
    return None  # No object found


# Example usage (replace with your image path)
image_path = cv2.imread("C:\\Users\\LENOVO\\Downloads\\sampleimg.jpeg")

extracted_object = threshold_segmentation(image_path)
extracted_text = extract_text(image_path)

if extracted_object is not None:
  cv2.imwrite("segment.png", extracted_object)
else:
  print("No object found in the image.")
    
html_content = f"""
<!DOCTYPE html>
<html>
<body>
  <h1>Extracted Text</h1>
  <p>{extracted_text}</p>
  <h2>Segmented Image</h2>
  <img height="300px" src='segment.png' alt='Segmented Image'>
</body>
</html>
  """
# Save HTML content
with open("output.html", "w") as f:
  f.write(html_content)

print("Analysis complete! Check output.html")
