from instapy import InstaPy
import cv2
import numpy as np
import os, pytesseract
import pyscreenshot as ImageGrab
import time, random, threading
from selenium.webdriver import Firefox

def change_size(self):
    window_size = self.browser.get_window_size()
    randx = 1100
    randy = 1100
    self.browser.set_window_size(window_size['width'] + randx, window_size['height'] + randy)
    return self



pytesseract.pytesseract.tesseract_cmd = 'path_to_tesseract.exe'
session = InstaPy(username="your_username", password="your_password", headless_browser=False)
change_size(session)
session.login()

def watch_story():
    session.story_by_users(["user_to_watch"])


filename = 'Image.png'



watch_story()
screen = np.array(ImageGrab.grab(bbox=(521, 70, 1464, 988)))
cv2.imwrite(filename, screen)
x = threading.Thread(target=watch_story)
    

img = cv2.imread('Image.png')
text = pytesseract.image_to_string(img)
print(text)
