# Image-analysis
The image analysis involves the extraction of text in the image and object in the image which is done by using Open-CV and Pytesseract modules. The Open-CV module is used to segement the image of the object present in the main image. pytesseract module is used to extract text from given image. This program is done to extract only single object from the main image. the segemented object will be stored in the same directory 

## Usage
### Step-1:
The analysis.py file contains the code required for analysis. this can be downloaded directly or clone the github repository by using following command
```
git clone https://github.com/8799ucs/Image-analysis.git
```
### Step-2:
The python-version 3.12.3. For running this file on local machine the following modules must be installed using pip commands and Tesseract OCR must be downloaded in order to work with pytesseract  
```
pip install opencv-python
pip install Pillow
pip install numpy
pip install pytesseract
```
### Step-3:
we must move to file where the repository exists 
```
cd Image-analysis
```
The execution or usage can be done by using following command in command prompt 
```
python analysis.py
```
if you want to execute using any other images change the image_path in the code. Hope this was helpful
