from PIL import Image
import pywhatkit as kit

ab= open("tet.txt","r")
info=ab.read()
kit.text_to_handwriting(info,save_to="handwriting.png")
Image.open("clcoding.png")